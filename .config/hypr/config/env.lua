-- ▄▄▄ . ▐ ▄  ▌ ▐·
-- ▀▄.▀·•█▌▐█▪█·█▌
-- ▐▀▀▪▄▐█▐▐▌▐█▐█•
-- ▐█▄▄▌██▐█▌ ███
--  ▀▀▀ ▀▀ █▪. ▀
--
-- https://wiki.hypr.land/Configuring/Advanced-and-Cool/Environment-variables/

local HOME = os.getenv("HOME")

-- Disables realtime priority setting by Hyprland. I Allready have ananicy
hl.env("HYPRLAND_NO_RT", "1")

hl.env("QT_QPA_PLATFORMTHEME", "hyprqt6engine")
