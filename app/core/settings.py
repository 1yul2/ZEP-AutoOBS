class AdminSettings:
    # Slack
    SLACK_ENABLED = True
    SLACK_DETECT_CAMERA = True
    SLACK_DETECT_JOIN_LEAVE = True
    SLACK_TARGET_NICKNAME = "한율"

    # ZEP
    ZEP_ENABLED = True
    ZEP_SUPER_ADMINS = {"한율"}

admin_settings = AdminSettings()