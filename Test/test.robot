*** Settings ***
Resource    common_resources.robot
Resource    test_resources.robot

*** Variables ***
${baseUrl}    ${url_ambiente_backend}

*** Test Cases ***
Get Status
    [Tags]    Smoke
    Create Session    mysession    ${baseUrl}
    ${response}=    GET On Session    mysession    ${endpoint_status}
    Status Should Be   Ok    ${response}

Get People List
    [Tags]    Smoke
    Create Session    mysession    ${baseUrl}
    ${response}=    GET On Session    mysession    ${endpoint_peoplelist}
    Status Should Be   Ok    ${response}
    ${json_response}=    To Json    ${response.content}
    Log To Console   ${json_response}
    Should Not Be Empty   ${json_response}   The response is empty

Add Person
    [Tags]    Smoke
    Create Session    mysession    ${baseUrl}
    ${person}=    Create Dictionary    name=John    lastname=Doe    age=30
    ${response}=    POST On Session    mysession    ${endpoint_addperson}    json=${person}
    Status Should Be   Created    ${response}
    ${json_response}=    To Json    ${response.content}
    Log To Console   ${json_response}

Get Person
    Create Session    mysession    ${baseUrl}
    ${last_person}=    Get last person
    ${response}=    GET On Session    mysession    ${endpoint_peoplelist}/${last_person}
    Status Should Be   Ok    ${response}
    ${json_response}=    To Json    ${response.content}
    ${person_id}=    Get From Dictionary    ${json_response}    id
    Should Be Equal    ${person_id}    ${last_person}

*** Keywords ***
Get last person
    Create Session    mysession    ${baseUrl}
    ${response}=    GET On Session    mysession    ${endpoint_peoplelist}
    ${length}=    Get Length    ${response.json()}
    ${last_person}=    Set Variable    ${response.json()}[${length-1}][id]
    Return From Keyword    ${last_person}