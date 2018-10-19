import requests
import json
import pprint
from jsontraverse.parser import JsonTraverseParser

API_KEY = 'SpzjlPZlkMlPKKGCLQS1OqZtCN96lPl7sszOTKra'
BASE_URL = 'https://api.propublica.org/congress/v1'
HEADERS = {
    'X-API-KEY': API_KEY
}


def get_specific_member(member_id):
    SPECIFIC_MEMBER_URL = BASE_URL + "/members/" + member_id + ".json"

    r = requests.get(url=SPECIFIC_MEMBER_URL, headers=HEADERS)
    data = r.json()
    return data


def get_member_information(member_results):
    # JsonTraverseParser needs a string
    json_string = json.dumps(member_results)

    # Get a JsonTraverseParser Object
    parser = JsonTraverseParser(json_string)
    member_id = parser.traverse("results.member_id")
    print(member_id)
    first_name = parser.traverse("results.first_name")
    last_name = parser.traverse("results.last_name")
    date_of_birth = parser.traverse("results.date_of_birth")
    url = parser.traverse("results.url")
    govtrack_id = parser.traverse("results.govtrack_id")
    cspan_id = parser.traverse("results.cspan_id")
    votesmart_id = parser.traverse("results.votesmart_id")
    icpsr_id = parser.traverse("results.icpsr_id")
    twitter_account = parser.traverse("results.twitter_account")
    facebook_account = parser.traverse("results.facebook_account")
    crp_id = parser.traverse("results.crp_id")
    in_office = parser.traverse("results.in_office")
    congress = parser.traverse("results.roles.congress")
    chamber = parser.traverse("results.roles.chamber")
    title = parser.traverse("results.roles.title")
    ocd_id = parser.traverse("results.roles.ocd_id")
    fec_candidate_id = parser.traverse("results.roles.fec_candidate_id")
    bills_sponsored = parser.traverse("results.roles.bills_sponsored")
    committee_names = parser.traverse("results.roles.committees.name")
    sub_committee_names = parser.traverse("results.roles.subcommittees.name")
    sub_committee_parent_id = parser.traverse("results.roles.subcommittees.parent_committee_id")

    legislator_container = []

    # Create a legislator
    legislator_data = {

        'member_id': member_id,
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
        'url': url,
        'govtrack_id': govtrack_id,
        'cspan_id': cspan_id,
        'votesmart_id': votesmart_id,
        'icpsr_id': icpsr_id,
        'twitter_account': twitter_account,
        'facebook_account': facebook_account,
        'crp_id': crp_id,
        'in_office': in_office,
        'congress': congress,
        'chamber': chamber,
        'title': title,
        'ocd_id': ocd_id,
        'fec_candidate_id': fec_candidate_id,
        'bills_sponsored': bills_sponsored,
        'committee_names': committee_names,
        'sub_committee_names': sub_committee_names,
        'sub_committee_parent_id': sub_committee_parent_id
    }

    legislator_container.append(legislator_data)

    return legislator_container
