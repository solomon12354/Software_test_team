*** Settings ***
Library    AppiumLibrary
Suite Setup    Open Application    http://127.0.0.1:4723    platformName=Android    automationName=UiAutomator2    deviceName=127.0.0.1:5555    appPackage=com.tonycube.app.movietime    appActivity=.view.LauncherActivity
Suite Teardown    Close Application

*** Variables ***
${shortPeriodOfTime} =    5s
${normalPeriodOfTime} =    10s
${longPeriodOfTime} =    15s

*** Test Cases ***
TVTC1
    [Setup]    Go To TV
    Click Element After It Is Visible    //*[@text='常用頻道']
    Wait Until Element Is Visible On Screen    //*[contains(@text, '目前沒有常用頻道')]
    Go Back
    Click Element After It Is Visible    //*[@text='戲劇']
    Click Element After It Is Visible    //*[@text='東森戲劇台']
    Click Element After It Is Visible    id=com.tonycube.app.movietime:id/menuAddFavoriteTv
    Go Back
    Wait Until Element Is Visible On Screen    //*[@text='東森戲劇台']/following-sibling::*[@content-desc='最愛的頻道']
    Go Back
    Click Element After It Is Visible    //*[@text='常用頻道']
    Wait Until Element Is Visible On Screen    //*[@text='東森戲劇台']
    [Teardown]    Return To Home

TVTC2
    [Setup]    Go To TV
    Click Element After It Is Visible    //*[@text='常用頻道']
    Click Element After It Is Visible    //*[@text='東森戲劇台']
    Click Element After It Is Visible    id=com.tonycube.app.movietime:id/menuRemoveFavoriteTv
    Go Back
    Go Back
    Click Element After It Is Visible    //*[@text='常用頻道']
    Wait Until Element Is Visible On Screen    //*[contains(@text, '目前沒有常用頻道')]
    [Teardown]    Return To Home

TVTC3
    [Setup]    Go To TV
    Click Element After It Is Visible    //*[@text='待看節目']
    Wait Until Element Is Visible On Screen    //*[contains(@text, '目前沒有待看節目')]
    Go Back
    Click Element After It Is Visible    //*[@text='戲劇']
    Click Element After It Is Visible    //*[@text='東森戲劇台']
    ${month}    ${day}    ${hour} =    Get Time    month day hour    NOW + 26h
    Click Element After It Is Visible    //*[contains(@text, '${month}-${day}')]
    ${status}    ${channelName} =    Run Keyword And Ignore Error    Get Text    //*[@text='${hour}:00']/parent::*/following-sibling::*[@resource-id='com.tonycube.app.movietime:id/txtProgramName']
    Run Keyword If    '${status}' == 'FAIL'    Swipe By Percent    start_x=50    start_y=80    end_x=50    end_y=20    duration=500
    ${channelName} =    Run Keyword If    '${status}' == 'FAIL'    Get Text    //*[@text='${hour}:00']/parent::*/following-sibling::*[@resource-id='com.tonycube.app.movietime:id/txtProgramName']
    ...                           ELSE    Set Variable    ${channelName}
    Set Suite Variable    ${channelName}
    Click Element After It Is Visible    //*[@text='${hour}:00']
    Wait Until Element Is Visible On Screen    id=com.tonycube.app.movietime:id/parentPanel
    Click Element After It Is Visible    //*[@text='只新增待看節目']
    Wait Until Page Does Not Contain Element    id=com.tonycube.app.movietime:id/parentPanel    timeout=${shortPeriodOfTime}
    Go Back
    Go Back
    Click Element After It Is Visible    //*[@text='待看節目']
    Wait Until Element Is Visible On Screen    //*[@text='${hour}:00']
    Wait Until Element Is Visible On Screen    //*[@text='${channelName}']
    Wait Until Element Is Visible On Screen    //*[@text='東森戲劇台']
    [Teardown]    Return To Home

TVTC4
    [Setup]    Go To TV
    Click Element After It Is Visible    //*[@text='待看節目']
    Wait Until Element Is Visible On Screen    //*[@text='${channelName}']
    Long Press Element    //*[@text='${channelName}']/parent::*
    Wait Until Element Is Visible On Screen   id=com.tonycube.app.movietime:id/parentPanel
    Click Element After It Is Visible    //*[@text='確定']
    Wait Until Page Does Not Contain Element    id=com.tonycube.app.movietime:id/parentPanel    timeout=${shortPeriodOfTime}
    Wait Until Element Is Visible On Screen    //*[contains(@text, '目前沒有待看節目')]
    [Teardown]    Return To Home

*** Keywords ***
Wait Until Element Is Visible On Screen
    [Arguments]    ${locator}
    Wait Until Page Contains Element    ${locator}    timeout=${shortPeriodOfTime}    error=Element should be visible.\n${locator}
    Wait Until Element Is Visible    ${locator}    timeout=${shortPeriodOfTime}    error=Element should be visible.\n${locator}

Click Element After It Is Visible
    [Arguments]    ${locator}
    Wait Until Element Is Visible On Screen    ${locator}
    Click Element    ${locator}

Return To Home
    ${returnBtn} =    Set Variable    //*[@content-desc='向上瀏覽']
    ${home} =    Run Keyword And Return Status    Page Should Not Contain Element    ${returnBtn}
    Run Keyword If    not ${home}    Run Keywords    Go Back
    ...                                       AND    Return To Home

Go To TV
    ${tvBtn} =    Set Variable    //*[@text='電視']
    Click Element After It Is Visible    ${tvBtn}

Long Press Element
    [Arguments]    ${locator}    ${duration}=1000
    ${location} =    Get Element Location    ${locator}
    ${location} =    Get Element Rect    ${locator}
    ${x} =    Evaluate    ${location}[x]+(${location}[width]/2)
    ${y} =    Evaluate    ${location}[y]+(${location}[height]/2)
    ${position} =    Create List    ${x}    ${y}
    Tap With Positions    ${duration}    ${position}