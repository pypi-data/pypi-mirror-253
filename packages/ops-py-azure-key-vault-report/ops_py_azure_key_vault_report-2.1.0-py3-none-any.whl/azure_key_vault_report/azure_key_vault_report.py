#!/usr/bin/env python

import logging
from datetime import datetime


########################################################################################################################


def set_timestamp(s, date_format=None):
    """Returns a date object of a string in format %Y-%m-%d.

    Parameters
    ----------
    s : str
        The date in string format
    date_format : str
        The expected format of the date string format.
        Please refer to https://strftime.org/

    Returns
    -------
    datetime.datetime object
        If the provided string ('s') parameter is not in valid format, None is returned.
    """

    if not date_format:
        date_format = "%Y-%m-%d"
    try:
        ts = datetime.strptime(str(s), date_format)
    except ValueError:
        logging.error(f"Unable to convert provided argument '{str(s)}' to timestamp object")
        return

    return ts

########################################################################################################################


class AzureKeyVaultReport(object):
    """generates a report from the results of 'az keyvault' commands

    The values of 'updated', 'created' and 'expires' are converted to date object
    and the age (in days) is calculated.

    Then a table is generated and sorted by (from top to bottom):
    the oldest 'Expiration' date, then by
    the oldest 'Last Updated' date


    Attributes
    ----------

    results : list
        The list of results from the 'az keyvault' commands, enriched with 'vault_name' and 'record_type'
    table_columns : list
        The list of table columns: a tuple of width and name for each column.
        Used in html and plain text report
    missing_expiration_date : int
        Counter for secret records which are missing an Expiration Date
    items : list
        The list of items.
        Items are enriched with more data, e.g. age of each date element, vault_name, record_type, record_name
    header : str
        The report header
    body : str
        The report body. Generated based on arguments passed to generate_report method and outcome of the az cli cmd
    footer : str
        The report footer, containing a summary.
    sep_line : str
        The dotted line which separates the header and footer. Length is calculated by column widths
    lm : str
        The left margin space
    this_year : int
        Counter for secret records that have been updated within the last 365 days
    one_year : int
        Counter for secret records updated within the range between age of 365 and 730 days
    two_years : int
        Counter for secret records updated within the range between age of 730 and 1095 days
    three_years : int
        Counter for secret records updated within the last 3 years
    facts : list
        The list of facts used in MS Teams output
    html_table : str
        The html table used in MS Teams output
    vaults : list
         The unique list of vaults processed


    Methods
    -------

    parse_results()
        Parse through the provided 'results' from the azure cli keyvault cmd outputs.
        For each result in the results new item is created and added to the items list.
        Each item contains the following data:
        - Date objects, created from the 'updated', 'created' and 'expires' values and stored as values
          in new X_ts keys.
        - The age (in days) is calculated from each of the date objects and stored as values in new X_age keys.
        - 'vault_name' and 'record_type
    set_report_header()
        Set the header part of the report:
        At the top row with dashes, then
        left aligned columns with fixed width, separated by |
        then a new row with dashes
    generate_report()
        Creates a plain text report and initiates ms team report generation if specified.
        The 'Comment' column created is generated according to the age of 'updated', 'created' and 'expires'.
        If missing 'expires' then a comment concerning that is also added.
    set_report_footer()
        set the stats in the plain text report footer
    sort_item():
        Returns a sorted list of all the records
    generate_html_table()
        Generates the html table
    add_html_row()
        Add row of record to html table
    get_html()
        Finalize the html table and returns it
    get_json_facts()
        Returns the facts (if any) to be used in the MS Teams JSON payload
    get_report()
        Returns the plain text report. Full report or summary only (the footer)
    """

    def __init__(self, results):
        """
        Parameters
        ----------
        results : list
            The list of results from the 'az keyvault' commands, enriched with 'vault_name' and 'record_type'
        """

        self.results = results
        self.table_columns = [
            (45, "Record Name"),
            (15, "Record Type"),
            (35, "Vault Name"),
            (15, "Last Updated"),
            (15, "Expiration"),
            (55, "Comment")
        ]
        self.missing_expiration_date = 0
        self.items = []
        self.header = ""
        self.body = ""
        self.footer = ""
        self.sep_line = ""    # A dotted line based on table column widths
        self.lm = " "         # Left margin
        self.this_year = 0    # Updated this year
        self.one_year = 0     # One year and older, but less than two years
        self.two_years = 0    # Two year and older, but less than three years
        self.three_years = 0  # Three years and older
        self.facts = []       # Facts to be used in an MS Teams payload
        self.html_table = ""  # HTML table to be used in an MS Teams payload
        self.vaults = []      # The unique list of vaults processed

    def parse_results(self):
        """parse through the result from the azure cli keyvault cmd output"""
        if not isinstance(self.results, list):
            return

        now = datetime.now()
        for r in self.results:
            for o in r.get("out"):
                item = {}
                if isinstance(o, dict):
                    vault_name = r.get("vault_name")
                    if vault_name not in self.vaults:
                        self.vaults.append(vault_name)

                    item["vault_name"] = vault_name
                    item["record_type"] = r.get("record_type")
                    item["record_name"] = o.get("name")

                    a = o.get("attributes")
                    if isinstance(a, dict):
                        for k, v in a.items():

                            if "enabled" in k:
                                item["enabled"] = v

                            if "updated" in k or "created" in k or "expires" in k and v:
                                value = v.split("T")[0]
                                item[k] = value
                                ts = set_timestamp(value)
                                item[f"{k}_ts"] = ts
                                age = (now - ts).days
                                item[f"{k}_age"] = age

                                # Update the update age counters:
                                # One year and older, but less than two years
                                if "updated" in k and age < 365:
                                    self.this_year += 1

                                # One year and older, but less than two years
                                if "updated" in k and (365 <= age < 365 * 2):
                                    self.one_year += 1

                                # Two year and older, but less than three years
                                elif "updated" in k and (365 * 2 <= age < 365 * 3):
                                    self.two_years += 1

                                # Three years and older
                                elif "updated" in k and age >= 365 * 3:
                                    self.three_years += 1

                self.items.append(item)

    def set_report_header(self):
        """set the header part of the report"""
        if not isinstance(self.results, list):
            return

        # Ensure the report variable is empty before heading is added to it
        self.header = ""

        # Create the dotted line part of the header. The length of the dotted row is each sum of chars from each column
        sep_line = ""
        for col in self.table_columns:
            sep_line += col[0] * "-"
        sep_line += "\n"
        self.sep_line = sep_line

        # Parse through each part of the header row. Element 0 is column total width. Element 1 is the actual value.
        header_row = ""
        for col in self.table_columns:
            header_row += f"| {col[1]: <{col[0]}}"

        # Add one dotted line row, the header row and one more dotted line row to the report
        self.header += self.sep_line
        self.header += f"{self.lm}{header_row.lstrip('| ')}"
        self.header += "\n"
        self.header += self.sep_line
        logging.info(f"header generated.")

    def sort_items(self, expired_days=7, will_expire_days=14):
        """Sort the list of dict items by days to expiration

        If no parameters provided, this method will return a sorted list of all the records.
        The list will be sorted from top and down, by the oldest 'Expiration' date and then followed
        by the oldest 'Last Updated' date and then returns the sorted list.

        If any of the parameters provided, it will first create and sort an 'expired' list and then the same with
        a 'will_expire' list, and the finally a list with the other records.
        Each list will be sorted from top and down, by the oldest 'Expiration' date and then followed
        by the oldest 'Last Updated' date and then returns a combined list.

        Parameters
        ----------
        expired_days : int
            If provided, the record will be added to a separate list (expired),
            if the expires_age (days since expiration) of the record
            is between 0 the days provided in the expired_days argument.

        will_expire_days : int
            If provided, the record will be added to a separate list (will_expire),
            if the expires_age (days to expiration) of the record
            is between 0 the days provided in the will_expire_days argument,
            and the record is not already added to the expired list.
        """

        if not isinstance(expired_days, int):
            return sorted(self.items, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)

        expired = []
        will_expire = []
        others = []
        for item in self.items:
            expires_age = item.get("expires_age")
            if isinstance(expires_age, int) and expires_age <= 0 and abs(expires_age) <= expired_days:
                expired.append(item)
                continue

            if isinstance(expires_age, int) and 0 <= expires_age <= will_expire_days:
                will_expire.append(item)
                continue

            others.append(item)

        sorted_list = sorted(expired, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)
        sorted_list += sorted(will_expire, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)
        sorted_list += sorted(others, key=lambda x: (str(x.get('expires')), x.get('updated', ' ')), reverse=False)

        return sorted_list

    def generate_report(self, expire_threshold=None, ignore_no_expiration=True, include_all=False, teams_json=False):
        """creates a plain text report and initiates ms team report generation if specified.
        returns the plain text report.

        Parameters
        ----------
        expire_threshold : int
            Ignore to report the record if days till the secret will expire are more than this 'expire_threshold' value
            NOTE: Secrets expiring today or already expired will always be reported.
        ignore_no_expiration : bool
            Report all records if set to False. If set to True only secrets with Expiration Date set will be reported.
        include_all : bool
            If set to True all records are included in the output.
        teams_json : bool
            If set to True then a report in json format containing a html table will also be generated.
        """
        if not isinstance(self.results, list):
            return

        if not self.header:
            self.set_report_header()

        # Ensure empty body
        self.body = ""

        # Sort the items from top and down
        # First sort by the oldest 'Expiration' date
        # Then sort by the oldest 'Last Updated' date
        items = self.sort_items()

        logging.info(f"expire_threshold: {expire_threshold} {type(expire_threshold)} - "
                     f"ignore_no_expiration: {ignore_no_expiration} ({type(ignore_no_expiration)}) - "
                     f"include_all: {include_all} {type(include_all)}")
        for item in items:
            row = ""

            # Get name of the record. If no name, we skip to next item in the list
            record_name = item.get("record_name")
            if not record_name:
                continue

            # Only list disabled entries if set to include_all
            enabled = item.get("enabled")
            if not include_all and not enabled:
                continue

            # Get the record type
            record_type = item.get("record_type", "")

            # Get the Vault Name
            vault_name = item.get("vault_name", "")

            # Get the expires and update values
            expires = item.get("expires", "")
            expires_age = item.get("expires_age")
            updated = item.get("updated")
            updated_age = item.get("updated_age")

            # Skip records with no Expiration Date set, only if 'ignore_no_expiration' and not 'include_all'
            if not expires:
                self.missing_expiration_date += 1
                if ignore_no_expiration and not include_all:
                    continue

            # Handle those with Expiration Date
            if isinstance(expires_age, int):

                # Handle those which has not expired yet
                if expires_age < 0:
                    logging.info(f"'{record_name}' has not expired yet. It will expire in {abs(expires_age)} days ({expires}).")

                    # Handle those within valid 'expire_threshold'
                    if isinstance(expire_threshold, int) and expire_threshold < abs(expires_age):
                        logging.info(f"'{record_name}' Expiration Date is within the valid specified threshold of "
                                     f"{expire_threshold} days. This record will start to be "
                                     f"reported in {abs(expires_age) - expire_threshold} days.")

                        # Only skipped if 'include_all' is not specified.
                        if not include_all:
                            continue

            # First column added is 'Record Name'. Second column is 'Last Updated'
            row += f"{self.lm}{record_name: <{self.table_columns[0][0]}}|"
            row += f"{self.lm}{record_type: <{self.table_columns[1][0]}}|"
            row += f"{self.lm}{vault_name: <{self.table_columns[2][0]}}|"
            row += f" {updated: <{self.table_columns[3][0]}}|"

            # Third column added is 'Expiration'. If 'Expiration' value is empty, blank spaces are added instead.
            if expires:
                row += f" {expires: <{self.table_columns[4][0]}}|"
            else:
                row += self.table_columns[4][0] * " "
                row += " |"

            # The last column 'Comment' has to be created before added to the row.
            # The value of 'Comment' is dependent of the info from the expires and update values
            comment = ""

            if not enabled:
                comment += "Disabled. "

            if isinstance(expires_age, int):
                if expires_age <= 0:
                    comment += f"Will expire in {abs(expires_age)} days. "
                if expires_age > 0:
                    comment += f"Expired {expires_age} days ago. "

            if not expires:
                comment += f"Has no expiration date. "

            if isinstance(updated_age, int):
                comment += f"Updated {updated_age} days ago. "

            # Finally the 'Comment' column is added to the row, along with a linebreak for the row
            row += f" {comment}\n"

            # A little cosmetic touch to avoid plural where it should not be used
            self.body += row.replace(" 1 days", " 1 day")

            # Generate json with html table to be used in Teams
            if teams_json:
                self.add_html_row(record_name, record_type, vault_name, updated, expires, comment)

        logging.info("report generated.")

        # Set the plain text report footer
        self.set_report_footer()

    def set_report_footer(self):
        """set the stats in the plain text report footer"""
        if not isinstance(self.results, list):
            return

        # Ensure footer starts with dotted line
        self.footer = self.sep_line

        # Add summary rows to the report
        if self.this_year:
            self.footer += f"{self.lm}Records updated in the last year.........: {self.this_year}\n"

        if self.one_year:
            self.footer += f"{self.lm}Records NOT updated in the last year.....: {self.one_year}\n"

        if self.two_years:
            self.footer += f"{self.lm}Records NOT updated for the last 2 years.: {self.two_years}\n"

        if self.three_years:
            self.footer += f"{self.lm}Records NOT updated for the last 3 years.: {self.three_years}\n"

        self.footer += f"{self.lm}Records missing Expiration Date..........: {self.missing_expiration_date}\n"
        self.footer += f"{self.lm}Total number of records..................: {len(self.items)}\n"
        self.footer += f"{self.lm}Total number of vaults...................: {len(self.vaults)}\n"
        self.footer += self.sep_line
        logging.info(f"footer generated.")

    def generate_html_table(self):
        """generates a html table to be used in json output for MS Teams"""
        self.html_table = f"""<table bordercolor='black' border='2'>
    <thead>
    <tr style='background-color : Teal; color: White'>
        <th>{self.table_columns[0][1]}</th>
        <th>{self.table_columns[1][1]}</th>
        <th>{self.table_columns[2][1]}</th>
        <th>{self.table_columns[3][1]}</th>
        <th>{self.table_columns[4][1]}</th>
        <th>{self.table_columns[5][1]}</th>
    </tr>
    </thead>
    <tbody>
    """

    def add_html_row(self, *args):
        """adds the table rows to html table"""
        if not self.html_table:
            self.generate_html_table()
        self.html_table += "<tr>"
        for arg in args:
            arg = arg.replace(". ", "<br>")
            self.html_table += f"<td>{arg}</td>"
        self.html_table += "</tr>"

    def get_html(self):
        """adding closing html tags and remove plural in days when it should not be used"""
        if self.html_table:
            self.html_table += "</tbody></table>"
            self.html_table = self.html_table.replace(" 1 days", " 1 day").replace("\n", "")

        return self.html_table

    def get_json_facts(self):
        """generates the fact used in the json output for MS Teams"""
        if not isinstance(self.results, list):
            return

        if len(self.items) == 0:
            return

        self.facts = [
            {"name": "Total number of Key Vaults:",
             "value": len(self.vaults)
             },
            {"name": "Total number of records:",
             "value": len(self.items)
             }
        ]

        if self.missing_expiration_date:
            self.facts.append(
                {"name": "Records missing Expiration Date:",
                 "value": self.missing_expiration_date
                 }
            )

        if self.this_year:
            self.facts.append(
                {"name": "Records updated in the last year:",
                 "value": self.this_year
                 }
            )

        if self.one_year:
            self.facts.append(
                {"name": "Records NOT updated in the last year:",
                 "value": self.one_year
                 }
            )

        if self.two_years:
            self.facts.append(
                {"name": "Records NOT updated for the last 2 years:",
                 "value": self.two_years
                 }
            )

        if self.three_years:
            self.facts.append(
                {"name": "Records NOT updated for the last 3 years:",
                 "value": self.three_years
                 }
            )

        logging.info(f"json summary generated.")

        return self.facts

    def get_report(self):
        """return the plain text report"""

        # If a body has been generated, then the header is also included in the output.
        if self.body:
            return self.header + self.body + self.footer

        # Only the summary footer is output when a body has not been generated.
        return self.footer
