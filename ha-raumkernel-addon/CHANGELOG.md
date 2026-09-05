## 1.2.37

- Fix uncaught UPnP 701 error when pausing a device that can't be paused (e.g. turning off/standby while on a TV/Line-in source or already stopped). `pause()` now swallows the expected 701 like `stop()` already did, so it no longer surfaces as an "Error processing message" stack trace. The related `Pause on ... failed` library log is also downgraded to debug.

## 1.2.36

- Merge upstream v1.2.18 fixes: Raumfeld devices sometimes failed to switch source when previously in Spotify Connect mode (#68); prevent add-on crashes in some situations, including when logging non-string error payloads (#69); add type and power-state guards for devices in standby/power-save mode; and faster virtual-zone creation when coming out of standby.

## 1.2.35

- Make the integration single-instance: adding it a second time is now rejected with "Already configured", regardless of the host/port entered. The previous 1.2.34 guard only blocked an identical host:port, so a second entry pointing at the same Raumfeld system via a different host string still slipped through and caused colliding unique IDs. Any existing duplicate entry must still be removed manually in Settings → Devices & Services.

## 1.2.34

- Prevent the integration from being configured twice for the same add-on instance (host:port). A duplicate config entry caused every room's entities to be registered twice, producing "does not generate unique IDs ... already exists - ignoring" errors in the log. Existing duplicate entries still need to be removed manually in Settings → Devices & Services.

## 1.2.33

- Publish pre-built multi-arch add-on images to `ghcr.io` via a new build workflow, and point the add-on at them with the `image:` option. Home Assistant now downloads a ready-made image instead of building it locally on the device, so updating shows a real download progress bar and installs much faster.

## 1.2.32

- Merge upstream maintenance release: upgrade dependencies (latest `node-raumkernel` fixes), and fix an add-on crash when sleep time is active.

## 1.2.31

- Merge upstream changes: fix track position/seek behavior, and changing the volume of a Raumfeld device in a group now affects only the selected device, not the whole group.

## 1.2.30

- Fix "Input" sensor for Soundbars/Sounddecks (devices with "Source Select"): now detects "Spotify"/"Radio" while streaming, instead of always showing "Streaming". "Source Select" only distinguishes physical inputs (Line-in, Optical, TV) from "Raumfeld" (streaming); when streaming, the playback URI is now inspected to tell Spotify Connect/Radio apart from regular Raumfeld zone playback.

## 1.2.29

- Bump version past the previously installed experimental build (1.2.28) so the integration auto-update is actually applied (auto-install only updates when the bundled version is newer than the installed one). No functional change beyond what was already in 1.2.21.

## 1.2.21

- Add a dynamic icon to the "Input" sensor matching the current source: `mdi:cast-audio` for Streaming, `mdi:audio-input-rca` for Line-in, `mdi:toslink` for Optical, `mdi:hdmi-port` for TV, `mdi:spotify` for Spotify, `mdi:radio` for Radio.

## 1.2.20

- Show an icon and the source name in the media player when there's no album art (e.g. Line-in, Optical, TV): `mdi:audio-input-rca` for Line-in, `mdi:toslink` for Optical, `mdi:hdmi-port` for TV.

## 1.2.19

- Fix the "Mute" state always showing as unmuted (`mdi:volume-high`), which made the media player's mute button only ever mute (never unmute), since the toggle always assumed the current state was unmuted. The UPnP `Mute` value is reported as the string `"0"`/`"1"`, not a number, so `state.Mute === 1` was always `false`.

## 1.2.18

- Update all `logo.png`/`dark_logo.png` files (add-on and `brand/` directories) with the new "Teufel | Raumfeld" logo versions, in both light and dark variants.

## 1.2.17

- Update all `logo.png`/`dark_logo.png` files (add-on and `brand/` directories) with the official "Teufel | Raumfeld" logo, in both light and dark variants.

## 1.2.16

- Update all `icon.png`/`dark_icon.png` files (add-on and `brand/` directories) with the official Raumfeld logo icon, in both light and dark variants.

## 1.2.15

- Replace `brand/` icon and logo with the official Raumfeld-branded images (256x256 icon, 600x200 logo), and add `dark_icon.png`/`dark_logo.png` light/dark variants per the HA Brands Proxy API.

## 1.2.14

- Add `selectSource` support for Soundbars and Sounddecks (TV_ARC, OpticalIn).
- Add Line-in switching for devices that don't support `Source Select` but have a physical Line-in input (e.g. Stereo M/L/R speakers).
- Add a separate "Eco mode" button per room, which puts the device into automatic standby (`EnterAutomaticStandby`) without affecting the existing "Off" button (`EnterManualStandby`).
- Add two new sensor entities per room: "Power status" (`Off` / `On` / `ECO mode`) and "Input" (current source: Streaming, Line-in, Optical, TV, Spotify, Radio).
- Track and broadcast the current "Source Select" value for soundbars/sounddecks, with periodic refresh to detect external changes (e.g. TV auto-switching to ARC).

Credits to contributor Simanias

## 1.2.13

- Fix track images which are hosted on Raumfeld devices (e.g. Local music, Tidal) not showing up.
- Add information/debug page to the addon (reachable at the default port).

## 1.2.12

- Added a setting to manually set the Raumfeld host address if auto discovery fails.

## 1.2.11

- Add support for media_content_id. It is now possible to see which media is currently playing.

## 1.2.10

- Fixes a crash if homeassistant sends a "prev" command even if prev is not allowed
- Fix issues with seek.

## 1.2.9

- Automatic install of integration

## 1.2.7

- Add Seek
- Improved Zone Handling
- Reboot Devices

## 1.2.2

- Add reboot feature to restart Raumfeld devices via SSH

## 1.0.0

- Initial release
