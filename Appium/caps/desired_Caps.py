capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.chrome',
    'appActivity': 'com.google.android.apps.chrome.Main',
    'language': 'en',
    'locale': 'US'
}

capabilities_v2 = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US'
}

desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'emulator-5554',
    'browser-name': 'Chrome',
    'appActivity': 'com.google.android.apps.chrome.Main',
    'chromeOptions': {
        'args': ['–disable-fre']}
    }


capabilities_v2 = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone.*',
    'app': 'storage:filename=SauceLabs-Demo-App-With-TestFairy.ipa',
    'sauce:options': {
        'username': 'oauth-luissndval-2d52a',
        'accessKey': '*****ccce',
        'build': 'appium-build-WAIJS',
        'name': '<your test name>'
    }
}

"""{
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
    "language": "en",
    "locale": "US"
}"""