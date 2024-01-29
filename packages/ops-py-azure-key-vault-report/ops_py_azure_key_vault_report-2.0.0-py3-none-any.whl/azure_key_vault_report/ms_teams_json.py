#!/usr/bin/env python

import json


########################################################################################################################


def get_json_output(title, facts, text):
    """add the facts and text to the json output for MS Teams, and then return the json output

    Parameters
    ----------
    title : str
        The 'activityTitle' which is the title of the message in MS Teams
    facts : list
        The list of 'facts' which is presented above the html table.
    text : str
        The text to be added below the 'facts'. The 'text' may be in html format.

    Returns
    -------
    json object
        A payload in json format. If not fact are provided, then None is returned.
    """

    if not facts:
        return

    json_output = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": "-",
        "sections": [
            {
                "activityTitle": title,
                "activitySubtitle": "",
                "activityImage": "",
                "facts": [],
                "markdown": True
            },
            {
                "startGroup": True,
                "text": ""
            }
        ]
    }

    json_output["sections"][0]["facts"] = facts
    json_output["sections"][1]["text"] = str(text)

    return json.dumps(json_output)
