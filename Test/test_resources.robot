*** Settings ***
*** Variables ***
#endpoints del Api
${endpoint_status}    /api/status
${endpoint_peoplelist}    /api/people
${endpoint_addperson}    /api/people
${endpoint_getperson}    /api/people/<int:id>
${endpoint_deleteperson}    /api/people/<int:id>
${endpoint_updateperson}    /api/people/<int:id>
*** Keywords ***