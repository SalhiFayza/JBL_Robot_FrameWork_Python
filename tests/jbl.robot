*** Settings ***
Documentation     JBL Headset Test Automation
Library           OperatingSystem
Library           Process
Resource          resources/variables.robot

*** Test Cases ***

Check if Headset is Connected
    ${bt}=    Run Process    python3 ./libraries/script_bluetooth.py ${MAC}    stdout=PIPE    shell=True
    ${status}=    Set Variable    ${bt.stdout.strip()}
    Log    Bluetooth Status: ${status}
    Run Keyword If    '${status}' != 'CONNECTED'    Fail    Headset is not connected

Play YouTube and Control Volume with Headset
    Run Process    python3 ./libraries/script_youtube_play.py ${YOUTUBE_LINK}    shell=True
    Log    YouTube and volume test completed

Check Headset Volume
    ${vol}=    Run Process    python3 ./libraries/script_volume.py    stdout=PIPE    shell=True
    ${volume}=    Set Variable    ${vol.stdout.strip()}
    Log    Volume Level: ${volume}
    Log To Console    Volume Level: ${volume}
    Run Keyword If    '${volume}' == '' or '${volume}' == 'NOT FOUND'    Fail    Volume not found
    Run Keyword If    not '${volume}'.isdigit()    Fail    Invalid volume value: ${volume}
