import os 
import requests 
import json

def scrape_linkedin_profile(linkedin_profile_url: str): 
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn Profile
    """
    # headers = {'Authorization': 'Bearer ' + os.environ.get("PROXYCURL_API_KEY")}
    # api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    # params = {
    #     'linkedin_profile_url': 'https://linkedin.com/in/mariephilippegill/',
    #     'fallback_to_cache': 'on-error',
    #     'use_cache': 'if-present',
    #     'skills': 'include',
    #     'inferred_salary': 'include',
    #     'personal_email': 'include',
    #     'personal_contact_number': 'include',
    #     'twitter_profile_id': 'include',
    #     'facebook_profile_id': 'include',
    #     'github_profile_id': 'include',
    #     'extra': 'include',
    # }
    # return requests.get(api_endpoint,
    #                         params=params,
    #                         headers=headers)

    # with open('eden-marco.json', 'r') as file:
    #     data = json.load(file)

    with open('output_linkedin copy.json', 'r') as file:
        data = json.load(file)
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data 