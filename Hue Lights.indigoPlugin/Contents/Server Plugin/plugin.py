#! /usr/bin/env python
# -*- coding: utf-8 -*-
####################
# Some code borrowed from the "Hue.indigoPlugin" (Hue Lighting Control) plugin
#   originally developed by Alistair Galbraith (alistairg on GitHub,
#   https://github.com/alistairg ).
#
#   His comment:
#   "This is UNSUPPORTED, AS-IS, open source code - do with it as you wish. Don't
#   blame me if it breaks! :)"
#
# His code base was forked on GitHub and completely rewritten by Nathan Sheldon
#   (nathan@nathansheldon.com)
#   http://www.nathansheldon.com/files/Hue-Lights-Plugin.php
#   All modificiations are open source.
#
#
#	Version 1.4.6b2
#
#
#				1.4.6b3.ag (alistairg)
#				Changed underlying approach to support multiple hue hubs. Each hub should be represented as its own device.
#				Added ability to recall scenes from the hue hub
#				--
#				1.4.6b2 (limited release).
#				* Changed light and group status update process to use less CPU in mid
#				  to large Hue installations.
#				--
#				1.4.6b1 (limited release).
#				* Fixed a potential bug in the startup code that may have caused an
#				  infinite device reload loop, and thus high CPU load.
#				* Fixed a bug that caused an error when attempting to edit Hue Groups
#				  device settings in the Indigo UI.
#				* Added some underlying code needed to support scenes and sensors, as well
#				  as other Hue features. Scenes and sensors are not yet supported, but
#				  it will now be easier to provide limited support in the future.
#				--
#				1.4.5
#				* Added automatic detection and loading of new lights and groups. No need
#				  to manually reload lights with the Reload Hue Device List menu item.
#				* Fixed a bug that incorrectly reported some updated devices as being out
#				  of date (from an old Hue Lights plugin version).
#				* Improved hue device status updating efficiency to reduce the number of
#				  Hue hub queries.
#				--
#				1.4.4
#				* Fixed another bug with Ambiance Lights Edit Device Settings dialog that
#				  would incorrectly show an error that the device wasn't an Ambiance Light.
#				1.4.3
#				* Fixed a bug with Ambiance Lights Edit Device Settings dialog that
#				  wouldn't allow you to save changes.
#				--
#				1.4.2
#				* Fixed a bug with Ambiance Lights selection list in Edit Device Settings
#				  dialog to not appear.
#				--
#				1.4.1
#				* Fixed a bug with LivingColors light update processing that caused
#				  the plugin to crash.
#				--
#				1.4.0
#				* Changed Hue Lights to now require Indigo 7 or later.
#				* Added support for color picker in light color setting actions.
#				* Added support for color and white temperature UI features in Indigo.
#				* Added Toggle Debugging menu item in Hue Lights plugin menu.
#				* Changed LightStrip Plus handling so it appears with the original
#				  Hue LigthStrip model in Edit Device Settings dialog.
#				* Updated Hue Group device name to show that it's no longer experimental.
#				--
#				1.3.30
#				* Fixed a bug in 1.3.29 that prevented Hue Lights from recognizing the
#				  2nd generation LightStrips.
#				--
#				1.3.29
#				* Added support for additional Hue light models.
#				--
#				1.3.28
#				* Added support for the Hue bulb v3, Hue White v2 and Hue White v3.
#				--
#				1.3.27
#				* Fixed a bug that caused a plugin crash when updating the status
#				  of a bulb that has no hue value associated with ti.
#				--
#				1.3.26
#				* Actually added the 2nd Hue White Ambiance model ID this time.
#				--
#				1.3.25
#				* Added support for 2 Hue White Ambiance bulb models.
#				* Fixed bug that caused the plugin to crash if a light had no
#				  color information from the Hue hub.
#				--
#				1.3.24
#				* Fixed a bug that caused the plugin to hang then crash after adding
#				  a Hue Group device.
#				--
#				1.3.23
#				* Added ability to use an Indigo variable for the ramp rate in all
#				  actions that have a ramp rate parameter.
#				* Added ability to use Indigo variables and other Indigo dimmers
#				  as the brightess source in actions that have a 0 to 100 percent
#				  scale brightness parameter (i.e. the "Set Hue/Saturation/Brightess"
#				  and "Set Color Temperature" actions. The "Set Brightness with
#				  Ramp Rate" action already had this capability).
#				* Added ability to use an Indigo variable for color temperature
#				  in the "Set Color Temperature" action.
#				--
#				1.3.22
#				* Fixed error when attempting to obtain device status from Osram
#				  CLA60 lights.  Light now appears as a Living Whites bulb.
#				* Improved light status gathering method to prevent plugin crashes
#				  if a light device doesn't have an expected property.
#				--
#				1.3.21
#				* Added support for the Osram Lightify CLA60 Tunable White bulb.
#				--
#				1.3.20
#				* Fixed the pairing process to work with hub firmware from 04-2016.
#				* Simplified hub pairing process (much less complicated now).
#				* Improved plugin configuration window error checking.
#				--
#				1.3.19
#				* Added support for new Phoenix light model.
#				--
#				1.3.18
#				* Fixed incompatibility with Indigo 6.1.8 that caused every
#				  HTTP connection to the Hue hub to generate a "Starting
#				  new HTTP connection (1)..." entry in the Indigo log.
#				--
#				1.3.17
#				* Updated Phoenix support so it appears in the LivingWhites
#				  device list instad of the color Hue bulbs list.
#				--
#				1.3.16
#				* Added support for the Phoenix wall lights.
#				--
#				1.3.15
#				* Moved supported device lists into a separate Python file
#				  for easier maintenance
#				* Added support for the Hue White A19 extension bulb.
#				--
#				1.3.14
#				* Added support for the new 800 lumen Hue bulb and the LED
#				  LightStrip Plus (temporarily found in the Hue Bulb list).
#				--
#				1.3.13
#				* Added support for the Dresden Elektronik FLS-PP lp LED strip
#				  white light segment.
#				--
#				1.3.12
#				* Added support for the Dresden Elektronik FLS-PP lp color
#				  LED light strip.
#				--
#				1.3.11
#				* Added Hue Go, Color Light, and Color Temperature modules to
#				  compatible device list.
#				--
#				1.3.10
#				* Fixed a bug that caused the plugine to crash when trying to
#				  obtain the "effect" state of a Hue Lux light on the hub.
#				--
#				1.3.9
#				* Fixed another bug that caused the plugin to crash if a Hue
#				  Group had no color mode defined on the Hue hub (e.g. all the
#				  group members were non-color bulbs).
#				--
#				1.3.8
#				* Added support for generic ZigBee lights such as the GE Link.
#				* Fixed a bug that caused the plugin to crash if an alert action
#				  was taken on a Hue Group device.
#				--
#				1.3.7
#				* Fixed a bug that caused the plugin to crash if there were
#				  any Hue groups registered with the Hue hub.
#				* Fixed a bug that prevented Hue Group devices from being
#				  loaded when the "Reload Hue Device List" plugin menu option
#				  was selected within the Indigo client.
#				--
#				1.3.6
#				* Added support for the Hue Lux bulb.
#				--
#				1.3.5
#				* Added support for the LivingColors Iris.
#				--
#				1.3.4
#				* Yet another attempt to fix the same bug found in 1.3.0.
#				--
#				1.3.3
#				* Another attempt to fix the same bug found in 1.3.0.
#				--
#				1.3.2
#				* Fixed a bug introduced in 1.3.1 that causes an error when
#				  no ramp rate is provided for Color Temperatur and other
#				  color change actions are initiated.
#				--
#				1.3.1
#				* Fixed a bug that could cause a plugin crash if a string
#				  was passed as the ramp rate in a Python script when
#				  executing any action that sets color.
#				--
#				1.3.0
#				* Added limited, experimental support for Hue groups.
#				  Support is limited to working with existing groups on
#				  the Hue hub. Hue groups are treated like other Hue
#				  devices.
#				* Minor error message corrections throughout the plugin.
#				--
#				1.2.11 (29-Apr-2014)
#				* Fixed a bug that would cause device edit dialogs to
#				  incorrectly report that the hub was not paired after
#				  the hub had been unreachable then became reachable again.
#				--
#				1.2.10 (23-Apr-2014)
#				* Fixed a bug that would cause the plugin to crash
#				  if a command was sent to the hub while the hub
#				  (or the plugin) was in an unstable state that
#				  resulted in an invalid pairing status.
#				* Updated the error reporting process so that major
#				  connection failure errors were actually reported as
#				  errors in the log rather than standard log entries.
#				* Updated the error reporting process so frequently
#				  displayed errors during a network or hub outage
#				  are reduced from once every 4 seconds to about once
#				  every minute.
#				--
#				1.2.9 (31-Mar-2014)
#				* Added support for the LivingColor Aura available
#				  in Europe (model ID LLC014).
#				* Updated Hue device types in Indigo device dialog
#				  to help clarify which device type to choose based
#				  on which Hue device you have.
#				--
#				1.2.8 (07-Feb-2014)
#				* Added support for the European version of the
#				  Bloom (model ID LLC011).
#				* Audited code to make sure all printable text is
#				  explicitly marked as Unicode text.
#				--
#				1.2.7 (10-Dec-2013)
#				* Added support for the Friends of Hue Disney
#				  StoryLight.
#				--
#				1.2.6 (21-Nov-2013)
#				* Added support for the Hue GU10 spot light.
#				* Increased number of Presets from 10 to 30.
#				--
#				1.2.5 (05-Nov-2013)
#				* Added support for the Hue "Downlight" BR30 bulb.
#				--
#				1.2.4 (10-Sep-2013)
#				* Added optional Ramp Rate to the Save Preset and Recall Preset
#				  actions and menu items.
#				* Fixed (hopefully) a bug that caused an ASCII translation error
#				  when editing an action for a device with non-ASCII characters
#				  in the name.
#				--
#				1.2.3 (04-Sep-2013... later that day.  :-) )
#				* Fixed a bug that caused a "typeId 'setBrightness'" error when
#				  attempting to create a Set Brightness with Ramp Rate action.
#				--
#				1.2.2 (04-Sep-2013)
#				* Increased the number of connection retries should a connection
#				  error be reported by the requests library.  Also disabled the
#				  HTTP "keep alive" connection pooling feature.
#				--
#				1.2.1 (02-Sep-2013)
#				* Fixed a bug that could cause the plugin to crash when using the
#				  Set Hue/Saturation/Brightness action from an external or embedded
#				  script then from an Indigo action.
#				* Added elipses to Plugins menu Preset items to conform to standard
#				  menu item naming convension when a dialog results from selecting
#				  a menu item.
#				--
#				1.2.0 (25-Aug-2013)
#				* Added Hue device settings Presets option that can save a device's
#				  current settings to be recalled (applied) later to any other
#				  compatible Hue device.
#				* Fixed a bug that would cause Hue devices to not turn off if the
#				  requested brightness level was 0 when using the Set RGB, Set HSB,
#				  Set Color Temperature, or Set xyY actions.
#				--
#				1.1.1 (20-Aug-2013)
#				* Added code to update device error states if a Hue device's online
#				  state changes to false, or there's some other kind of error.
#				* Corrected some UI labeling errors.
#				--
#				1.1.0 (18-Aug-2013)
#				* Added support for the following Friends of Hue devices:
#				     - LightStrips
#				     - LivingColors Bloom
#				* Added experimental support for LivingWhites devices.
#				* Fixed a bug that wouldn't turn off the Hue bulb as quickly if using
#				  the standard device Turn Off command as opposed to setting the
#				  brightness to 0 method.
#				* Updated the Set Red/Green/Blue function to better match
#				  Hue device capabilities.
#				* Added a Set xyY Chromaticity (Advanced) action that allows one to
#				  directly specify the x/y chromaticity and Y luminosity values for
#				  devices that can render color.
#				--
#				1.0.3 (09-Aug-2013)
#				* Fixed bug that caused the plugin to crash when using a LightStrip
#				  device.
#				--
#				1.0.2 (09-Aug-2013)
#				* Added ability to recognize new LightStrips and "wall washer" strips.
#				--
#				1.0.1 (30-Jul-2013)
#				* Added the indigoPluginUpdateChecker module (code by Travis CooK)
#				  to facilitate automatic plugin version checking.
#				--
#				1.0 (03-Jul-2013)
#				* Updated brightness status code to accurately reflect a 1
#				  percent brightness level (rather than rounding up to 2 percent).
#				* Added Default Brightness property for Hue Bulbs devices so
#				  their features are more consistent with other lighting devices
#				  in Indigo (such as SwitchLinc and LampLinc Dimmers).
#				* Changed "on", "off", and "toggle" action control functions so
#				  that sending an "on" command to a Hue Bulb from within Indigo
#				  returns the bulb to its previous brightness level, or its
#				  default brightness level (if set).
#				* Updated Brightness, HSB, and Color Temperature setting methods
#				  so that they properly save the brightness level specified in
#				  those actions to the Hue Bulb's device properties for recall
#				  should an "on" command be sent to it.
#				* Updated the bulb status gathering method so that if the bulb
#				  brightness changes outside of the Hue Lights plugin (or the hub
#				  updates the bulb brightness during a long transition time),
#				  Hue Lights does not save the new brightness to the bulb
#				  properties and thus causing an "on" command later to recall an
#				  incorrect previous brightness state.
#				* Changed the logging slightly to more closely match the log
#				  format of native INSTEON device changes.
#				--
#				0.10.2 (24-Jun-2013)
#				* Added more code to work better with LivingWhites bulbs.
#				--
#				0.10.1 (24-Jun-2013)
#				* Modified debugging code so it wouldn't throw errors when the
#				  plugin is installed on versions of Indigo Pro earlier than
#				  version 5.1.7.
#				* Added the LWB003 model ID to the list of recognized Hue models.
#				--
#				0.10.0 (12-Jun-2013)
#				* Added a Hue Bulb Attribute Controller virtual dimmer device
#				  which can be created to control a specific attribute (hue,
#				  saturation, RGB levels, or color temperature) of an existing
#				  Hue Lights bulb device.
#				* Added an "Effect" action which allows you to specify an effect
#				  to be turned on for a Hue bulb (requires latest firmware on
#				  the Hue hub. Currently, only the Color Loop effect is supported
#				  by the Hue hub and bulbs).
#				* Changed light control methods so that if the current light
#				  brightness is below 6% and the requested action is to turn off
#				  the bulb, set the ramp rate to 0 regardless of the default or
#				  specified ramp rate (transition time) because going from a
#				  brightness of 6% or lower to an off state with a dimming rate
#				  isn't noticeable.
#				--
#				0.9.11 (10-Apr-2013)
#				* Updated code to more elegantly handle non-Hue devices attached
#				  to the Hue hub.
#				--
#				0.9.10 (02-Apr-2013)
#				* Fixed a bug that would cause the plugin to crash if a
#				  registered bulb on the Hue hub had no "hue" attribute (which
#				  could happen when using "LivingWhites" plugin dimmers found in
#				  some European countries).
#				--
#				0.9.9 (24-Jan-2013)
#				* Attempted to make RGB-to-xyY conversions more accurate by
#				  changing the illuminant used by the colormath functions from
#				  type "a" to type "e".
#				--
#				0.9.8 (23-Jan-2013)
#				* Fixed a bug that would crash the plugin if no device was
#				  selected in a start/stopBrightening/Dimming action when the
#				  action was executed.
#				* Fixed a bug that would cause an error during device creation
#				  dialog validation for new Hue Light devices in Indigo 5.x.
#				--
#				0.9.7 (31-Dec-2012)
#				* Fixed a bug that updated the "hue" state of plugin devices
#				  with an invalid number when the setHSB action was used.
#				--
#				0.9.6 (31-Dec-2012)
#				* Fixed a divide by zero error in getBulbStatus that could
#				  happen if the Hue hub returns no value for a blub's color
#				  temperature.
#				--
#				0.9.5 (27-Dec-2012)
#				* Fixed bug that would cause the Hue light not to turn off
#				  if using RGB mode when Red, Green, and Blue were all zero.
#				--
#				0.9.4 (27-Nov-2012)
#				* Fixed bug that would return an error if no default ramp
#				  rate were enered for a Hue bulb device.
#				* Added more debug logging.
#				* Changed how logging is done to be more consistant with
#				  other Indigo device update events. A log entry now appears
#				  after the physical device has changed (as was always the
#				  case) but now it appears before the Indigo device state
#				  is updated.
#				* Increased delay between status update requests to about
#				  8 seconds to decrease number of requests per minute
#				  sent to the Hue hub.
#				--
#				0,9.3 (18-Nov-2012)
#				* Fixed typo (bug) that caused the plugin to crash when the
#				  Hue hub was unreachable within the timeout period.
#				* Worked around a colormath bug that would throw a
#				  ZeroDivisionError if the "y" component was zero.
#				* Added checks in bulb status gathering to prevent unnecessary
#				  Indigo device status updates. Added logging for any device
#				  brightness updates detected.
#				* Added more exception handling for HTTP requests to hub.
#				* Slightly tweaked status request timing.
#				--
#				0.9.2 (17-Nov-2012)
#				* Corrected error in actionControlDimmerRelay that prevented
#				  setBrightness call from working.
#				--
#				0.9.1 (16-Nov-2012)
#				* Tweaked brightening and dimming timing for Start Brightening
#				  and Start Dimming actions so the rate was about the same speed
#				  as SmartLabs SwithcLinc Dimmers and LampLinc Dimmers.
#				* Removed code that immediately changes the RGB color states for
#				  the Indigo device as the values entered by the user are not
#				  actual displayed values. Actual values will be updated by the
#				  getBulbStatus method later.
#				* Added the "Set Brightness with Ramp Rate" action and associated
#				  plugin.py code. Renamed multiple methods for easier redability
#				  and for easier plugin scripting within Indigo.  Reorganized
#				  order in which methods appear in the source code for a more
#				  logical layout.
#				--
#				0.9 (13-Nov-2012)
#				* Initial Nathan Sheldon forked beta release.
#				* This version removes the use of the "ColorPy" library from
#				  Alistair's version and replaces it with the "colormath"
#				  library as it includes the ability to specify a target
#				  illumination source during color conversion, thus presenting
#				  a closer RGB to xyY conversion (and vice-versa).
#				* Most of Alistair's original code was rewritten to remain
#				  consistent with coding convensions in my other plugins, but
#				  some of his code is still in here.
#
################################################################################

import os
import sys
import logging
import requests
import socket
from colormath.color_objects import RGBColor, xyYColor, HSVColor
from math import ceil, floor
import simplejson as json
import indigoPluginUpdateChecker
from supportedDevices import *

# Default timeout.
kTimeout = 4		# seconds
# Default connection retries.
requests.defaults.defaults['max_retries'] = 3
# Turn off the HTTP connection "keep alive" feature.
requests.defaults.defaults['keep_alive'] = False
# Set the Python logging level to "WARNING" to override the Requests library
#   default of "INFO", which causes a log entry in Indigo 6.1.8+ for every
#   HTTP connection made to the Hue hub.
logging.getLogger("requests").setLevel(logging.WARNING)


################################################################################
class Plugin(indigo.PluginBase):
	########################################
	# Loading and Starting Methods
	########################################

	# Load Plugin
	########################################
	def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
		indigo.PluginBase.__init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
		self.debug = pluginPrefs.get('showDebugInfo', False)
		self.debugLog(u"Initializing Plugin.")
		self.deviceList = []		# list of device IDs to monitor
		self.hubList = []			# list of hub definitions
		self.controlDeviceList = []	# list of virtual dimmer device IDs that control bulb devices
		self.brighteningList = []	# list of device IDs being brightened
		self.dimmingList = []		# list of device IDs being dimmed
		self.paired = False			# if paired with Hue hub or not
		self.lastErrorMessage = u""	# last error message displayed in log
		self.hueConfigDict = dict()	# Entire Hue hub configuration dictionary.
		self.lightsDict = dict()	# Hue devices dict.
		self.groupsDict = dict()	# Hue groups dict.
		self.resourcesDict = dict()	# Hue resource links dict.
		self.sensorsDict = dict()	# Hue sensors dict.
		self.usersDict = dict()		# Hue users dict.
		self.scenesDict = dict()	# Hue scenes dict.
		self.rulesDict = dict()		# Hue trigger rules dict.
		self.schedulesDict = dict()	# Hue schedules dict.
		self.unsupportedDeviceWarned = False	# Boolean. Was user warned this device isn't supported?
		# Load the update checker module.
		self.updater = indigoPluginUpdateChecker.updateChecker(self, 'http://www.nathansheldon.com/files/PluginVersions/Hue-Lights.html')

	# Unload Plugin
	########################################
	def __del__(self):
		indigo.PluginBase.__del__(self)

	# Startup
	########################################
	def startup(self):
		self.debugLog(u"Startup called.")
		# Perform an initial version check.
		self.debugLog(u"Running plugin version check (if enabled).")
		self.updater.checkVersionPoll()

		# Prior to version 1.2.0, the "presets" property did not exist in the plugin preferences.
		#   If that property does not exist, add it.
		# As of version 1.2.6, there are now 30 presets instead of 10.
		if not self.pluginPrefs.get('presets', False):
			self.debugLog(u"pluginPrefs lacks presets.  Adding.")
			# Add the empty presets list to the prefs.
			self.pluginPrefs['presets'] = list()
			# Start a new list of empty presets.
			presets = list()
			for aNumber in range(1,31):
				# Create a blank sub-list for storing preset name and preset states.
				preset = list()
				# Add the preset name.
				preset.append('Preset ' + str(aNumber))
				# Add the empty preset states Indigo dictionary
				preset.append(indigo.Dict())
				# Add the sub-list to the empty presets list.
				presets.append(preset)
			# Add the new list of empty presets to the prefs.
			self.pluginPrefs['presets'] = presets
			self.debugLog(u"pluginPrefs now contains 30 presets.")
		# If presets exist, make sure there are 30 of them.
		else:
			presets = self.pluginPrefs.get('presets', "")
			presetCount = len(presets)
			self.debugLog(u"pluginPrefs contains " + str(presetCount) + u" presets.")
			if presetCount < 30:
				self.debugLog(u"... Adding " + str(30 - presetCount) + u" presets to bring total to 30.")
				for aNumber in range(presetCount + 1,31):
					# Add ever how many presets are needed to make a total of 30.
					# Create a blank sub-list for storing preset name and preset states.
					preset = list()
					# Add the preset name.
					preset.append('Preset ' + str(aNumber))
					# Add the empty preset states Indigo dictionary
					preset.append(indigo.Dict())
					# Add the sub-list to the empty presets list.
					presets.append(preset)
				# Add the new list of empty presets to the prefs.
				self.pluginPrefs['presets'] = presets
				self.debugLog(u"pluginPrefs now contains 30 presets.")
		self.debugLog(u"pluginPrefs are:\n" + str(self.pluginPrefs))


	# Start Devices
	########################################
	def deviceStartComm(self, device):
		self.debugLog(u"Starting device: " + device.name)
		# Clear any device error states first.
		device.setErrorStateOnServer("")

		# Prior to version 1.1.0, the "modelId" property did not exist in lighting devices.
		#   If that property does not exist, force an update.
		if device.deviceTypeId != "hueHub" and device.deviceTypeId != "hueAttributeController" and device.deviceTypeId != "hueGroup" and not device.pluginProps.get('modelId', False):
			self.debugLog(u"The " + device.name + u" device doesn't have a modelId attribute.  Adding it.")
			newProps = device.pluginProps
			newProps['modelId'] = ""
			device.replacePluginPropsOnServer(newProps)

		# Prior to version 1.3.8, the "alertMode" state didn't exist in Hue Group devices.
		#   If that state does not exist, force the device state list to be updated.
		if device.deviceTypeId != "hueHub" and device.deviceTypeId == "hueGroup" and not device.states.get('alertMode', False):
			self.debugLog(u"The " + device.name + u" device doesn't have an alertMode state.  Updating device.")
			device.stateListOrDisplayStateIdChanged()

		# Prior to version 1.4, the color device properties did not exist in lighting devices.
		#   If any of those properties don't exist, notify the user to redefine the device in Indigo.
		if device.deviceTypeId != "hueAttributeController" and device.pluginProps.get('modelId', "") != "" and device.pluginProps['modelId'] not in kLivingWhitesDeviceIDs:
			if device.pluginProps['modelId'] in kAmbianceDeviceIDs and not device.supportsWhite:
				self.debugLog(u"The \"" + device.name + u"\" Ambiance light device doesn't have color temperature properties.")
				self.errorLog(u"The \"" + device.name + u"\" device is from an old Hue Lights version. Double-click on the device in Indigo, click \"Edit Device Settings\", then click \"Save\" and close the \"Edit Device\" window.")
			elif not device.supportsRGB:
				self.debugLog(u"The \"" + device.name + u"\" color light device doesn't have color properties.")
				self.errorLog(u"The \"" + device.name + u"\" device is from an old Hue Lights version. Double-click on the device in Indigo, click \"Edit Device Settings\", then click \"Save\" and close the \"Edit Device\" window.")

		# Version 1.4+ handles the original LightStrip and newer LightStrip Plus using the same
		#   deviceTypeId, but they have different capabilities.  If this is an original LightStrip,
		#   remove the color temperature properties from this device.
		if device.deviceTypeId == "hueLightStrips" and device.pluginProps['modelId'] == "LST001":
			self.debugLog(u"The " + device.name + u" is an original LightStrip device. Updating device properties to reflect lack of color temperature support.")
			newProps = device.pluginProps
			if device.supportsWhite:
				newProps['SupportsWhite'] = False
			if device.supportsWhiteTemperature:
				newProps['SupportsWhiteTemperature'] = False
			if device.supportsRGBandWhiteSimultaneously:
				newProps['SupportsRGBandWhiteSimultaneously'] = False
			device.replacePluginPropsOnServer(newProps)

		# Update the core lists of the hub as it starts
		if device.deviceTypeId == "hueHub":
			hueUsername = device.pluginProps.get("hostId", None)
			if hueUsername is None:
				self.debugLog(u"Hue Lights doesn't appear to be paired with the Hue hub.")
			else:
				self.debugLog(u"The username Hue Lights uses to connect to the Hue hub '%s' is %s" % (device.name, hueUsername))
			self.updateAllHueLists(device)

		# Update the device lists and the device states.
		# Hue Device Attribute Controller
		if device.deviceTypeId == "hueAttributeController":
			if device.id not in self.controlDeviceList:
				try:
					self.debugLog(u"Attribute Control device definition:\n" + str(device))
				except Exception, e:
					self.debugLog(u"Attribute Control device definition cannot be displayed because: " + str(e))
				self.controlDeviceList.append(device.id)
		# Hue Groups
		elif device.deviceTypeId == "hueGroup":
			if device.id not in self.deviceList:
				try:
					self.debugLog(u"Hue Group device definition:\n" + str(device))
				except Exception, e:
					self.debugLog(u"Hue Group device definition cannot be displayed because: " + str(e))
				self.deviceList.append(device.id)
				# Get the group's status.
				self.getGroupStatus(device.id)
		# Hue Hubs
		elif device.deviceTypeId == "hueHub":
			if device.id not in self.hubList:
				try:
					self.debugLog(u"Hue Hub device definition:\n" + str(device))
				except Exception, e:
					self.debugLog(u"Hue Hub device definition cannot be displayed because: " + str(e))
				self.hubList.append(device.id)
		# Other Hue Devices
		else:
			if device.id not in self.deviceList:
				try:
					self.debugLog(u"Hue device definition:\n" + str(device))
				except Exception, e:
					# With versions of Indigo sometime prior to 6.0, if any device name had
					#   non-ASCII characters, the above "try" will fail, so we have to show
					#   this error instead of the actual bulb definition.
					self.debugLog(u"Hue device definition cannot be displayed because: " + str(e))
				self.deviceList.append(device.id)

	# Stop Devices
	########################################
	def deviceStopComm(self, device):
		self.debugLog(u"Stopping device: " + device.name)
		if device.deviceTypeId == "hueAttributeController":
			if device.id in self.controlDeviceList:
				self.controlDeviceList.remove(device.id)
		else:
			if device.id in self.deviceList:
				self.deviceList.remove(device.id)

	# Shutdown
	########################################
	def shutdown(self):
		self.debugLog(u"Plugin shutdown called.")


	########################################
	# Standard Plugin Methods
	########################################

	# New Device Created
	########################################
	def deviceCreated(self, dev):
		self.debugLog(u"Created device of type \"%s\"." % dev.deviceTypeId)

	# Run a Concurrent Thread for Status Updates
	########################################
	def runConcurrentThread(self):
		self.debugLog(u"runConcurrentThread called.")
		#
		# Continuously loop through all Hue lighting devices to see if the
		#   status has changed.
		#

		j = 0	# Used to reset lastErrorMessage value every 8 loops.

		try:
			while True:
				# Check for newer plugin versions.
				self.updater.checkVersionPoll()

				## Brightening Devices ##
				i = 0	# Used to gage timing of brightening or dimming loops.
				# Loop 20 times (about 0.4 sec per loop, 8 sec total).
				while i < 20:
					# Go through the devices waiting to be brightened.
					for brightenDeviceId in self.brighteningList:
						# Make sure the device is in the deviceList.
						if brightenDeviceId in self.deviceList:
							# Increase the brightness level by 10 percent.
							brightenDevice = indigo.devices[brightenDeviceId]
							brightness = brightenDevice.states['brightnessLevel']
							self.debugLog(u"Brightness: " + str(brightness))
							brightness += 12
							self.debugLog(u"Updated to: " + str(brightness))
							if brightness >= 100:
								brightness = 100
								# Log the event to Indigo log.
								indigo.server.log(u"\"" + brightenDevice.name + "\" stop brightening", 'Sent Hue Lights')
								self.brighteningList.remove(brightenDeviceId)

								# Get the hub device
								hubId = brightenDevice.pluginProps.get("hubId", None)
								hubDevice = None
								if hubId is not None:
									hubDevice = indigo.devices.get(int(hubId), None)

								# Get the bulb status (but only if paired with the hub).
								if hubDevice is not None and hubDevice.pluginProps.get("paired", False) == True:
									self.getBulbStatus(brightenDeviceId)
									# Log the new brightnss.
									indigo.server.log(u"\"" + brightenDevice.name + "\" status request (received: 100)", 'Sent Hue Lights')
								else:
									self.debugLog(u"Not currently paired with Hue hub. Status update skipped.")
							# Convert percent-based brightness to 255-based brightness.
							brightness = int(round(brightness / 100.0 * 255.0))
							# Set brightness to new value, with 0.5 sec ramp rate and no logging.
							self.doBrightness(brightenDevice, brightness, 0.5, False)

					# Go through the devices waiting to be dimmed.
					for dimDeviceId in self.dimmingList:
						# Make sure the device is in the deviceList.
						if dimDeviceId in self.deviceList:
							# Decrease the brightness level by 10 percent.
							dimDevice = indigo.devices[dimDeviceId]
							brightness = dimDevice.states['brightnessLevel']
							brightness -= 12
							if brightness <= 0:
								brightness = 0
								# Log the event to Indigo log.
								indigo.server.log(u"\"" + dimDevice.name + u"\" stop dimming", 'Sent Hue Lights')
								self.dimmingList.remove(dimDeviceId)

								# Get the hub device
								hubId = brightenDevice.pluginProps.get("hubId", None)
								hubDevice = None
								if hubId is not None:
									hubDevice = indigo.devices.get(int(hubId), None)

								# Get the bulb status (but only if we're paired with the hub).
								if hubDevice is not None and hubDevice.pluginProps.get("paired", False) == True:
									self.getBulbStatus(dimDeviceId)
									# Log the new brightnss.
									indigo.server.log(u"\"" + dimDevice.name + u"\" status request (received: 0)", 'Sent Hue Lights')
								else:
									self.debugLog(u"Not currently paired with Hue hub. Status update skipped.")
							# Convert percent-based brightness to 255-based brightness.
							brightness = int(round(brightness / 100.0 * 255.0))
							# Set brightness to new value, with 0.5 sec ramp rate and no logging.
							self.doBrightness(dimDevice, brightness, 0.5, False)

					# Wait for 0.4 seconds before loop repeats.
					self.sleep(0.4)
					# Increment loop counter.
					i += 1

				# If the error clearing loop counter has reached 8 (about 64 seconds
				#    have passed), then clear the lastErrorMessage and reset the loop.
				if j >= 8:
					self.lastErrorMessage = u""
					j = 0
				else:
					# Error clearing loop counter not yet complete, increment the value.
					j += 1

				# Now that the brightening/dimming loop has finished, get device states for each hub
				for hubId in self.hubList:
					hubDevice = indigo.devices.get(hubId, None)
					if hubDevice is not None:
						self.updateLightsList(hubDevice)
						self.parseHueLightsData(hubDevice)
						self.updateGroupsList(hubDevice)
						self.parseHueGroupsData(hubDevice)
					else:
						self.errorLog("Failed to get a hub with id '%i'" % hubId)

		except self.StopThread:
			self.debugLog(u"runConcurrentThread stopped.")
			pass

		self.debugLog(u"runConcurrentThread exiting.")


	# Color Picker Dialog Methods
	#   (based on code from Matt Bendiksen)
	########################################
	def isIntCompat(self, someValue):
		# Check if a value is an integer or not.
		try:
			if type(someValue) == int:
				# It's already an integer. Return right away.
				return True
			# It's not an integer, so try to convert it to one.
			int(unicode(someValue))
			# It converted okay, so return True.
			return True
		except (TypeError, ValueError):
			# The value didn't convert to an integer, so return False.
			return False

	def calcRgbHexValsFromRgbLevels(self, valuesDict):
		# Convert RGB integer values to RGB hex values.
		rgbHexVals = []
		for channel in ['red', 'green', 'blue']:
			fieldValue = 0
			# Make sure the field values are integers.
			if channel in valuesDict and self.isIntCompat(valuesDict[channel]):
				fieldValue = int(valuesDict[channel])
			# Make sure the values are within valid limites.
			if fieldValue < 0:
				fieldValue = 0
			elif fieldValue > 255:
				fieldValue = 255
		# Convert integers to hexadecimal values.
		rgbHexVals.append("%02X" % fieldValue)
		# Return all 3 values as a string separated by a single space.
		return ' '.join(rgbHexVals)

	def calcRgbHexValsFromHsbLevels(self, valuesDict):
		# Convert HSB integer values to RGB hex values.
		rgbHexVals = []
		hue = 0
		saturation = 0
		brightness = 0
		brightnessSource = valuesDict.get('brightnessSource', "custom")
		brightnessDevId = int(valuesDict.get('brightnessDevice', 0))
		brightnessVarId = int(valuesDict.get('brightnessVariable', 0))

		for channel in ['hue', 'saturation', 'brightness']:
			fieldValue = 0
			# Make sure the field values are integers.
			if channel in valuesDict and self.isIntCompat(valuesDict[channel]):
				fieldValue = int(valuesDict[channel])
			# Make sure the values are within valid limites.
			if fieldValue < 0:
				fieldValue = 0
			if channel == 'hue':
				if fieldValue > 360:
					fieldValue = 360
				hue = fieldValue
			elif channel == 'saturation':
				if fieldValue > 100:
					fieldValue = 100
				saturation = fieldValue
			elif channel == 'brightness':
				# If the brightnessSource is something other than "custom" get the current
				#   value of the device or variable to which the brightness should be derived.
				if brightnessSource == "variable":
					fieldValue = indigo.variables[brightnessVarId].value
					if self.isIntCompat(fieldValue):
						fieldValue = int(fieldValue)
				elif brightnessSource == "dimmer":
					fieldValue = indigo.devices[brightnessDevId].brightness
					if self.isIntCompat(fieldValue):
						fieldValue = int(fieldValue)
				if fieldValue > 100:
					fieldValue = 100
				brightness = fieldValue
		# Convert from HSB to RGB.
		hsb = HSVColor(hue, saturation / 100.0, brightness / 100.0)
		rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
		red = int(round(rgb.rgb_r))
		green = int(round(rgb.rgb_g))
		blue = int(round(rgb.rgb_b))
		# Convert integers to hexadecimal value while appending it to the rbgHexVals tuple.
		rgbHexVals.append("%02X" % red)
		rgbHexVals.append("%02X" % green)
		rgbHexVals.append("%02X" % blue)
		# Return all 3 values as a string separated by a single space.
		return ' '.join(rgbHexVals)

	def rgbColorPickerUpdated(self, valuesDict, typeId, devId):
		self.debugLog(u"rgbColorPickerUpdated called.")
		self.debugLog(u"typeId: " + typeId + "\ndevId: " + str(devId) + "\nvaluesDict: " + str(valuesDict))
		# Get the raw 3 byte, space-separated hex string from the color picker.
		rgbHexList = valuesDict['rgbColor'].split()
		# Assign the RGB values.
		red = int(rgbHexList[0], 16)
		green = int(rgbHexList[1], 16)
		blue = int(rgbHexList[2], 16)
		# Convert the RGB values to HSL/HSV for use in the HSB actions.
		rgb = RGBColor(red, green, blue, rgb_type='wide_gamut_rgb')
		hsb = rgb.convert_to('hsv')
		hue = int(round(hsb.hsv_h * 1.0))
		saturation = int(round(hsb.hsv_s * 100.0))
		brightness = int(round(hsb.hsv_v * 100.0))

		# Assign the values to the appropriate valuesDict items.
		valuesDict['red'] = red
		valuesDict['green'] = green
		valuesDict['blue'] = blue
		valuesDict['hue'] = hue
		valuesDict['saturation'] = saturation
		valuesDict['brightness'] = brightness

		# Can send a live update to the hardware here:
		#    self.sendSetRGBWCommand(valuesDict, typeId, devId)

		del valuesDict['rgbColor']
		return (valuesDict)

	def rgbColorFieldUpdated(self, valuesDict, typeId, devId):
		self.debugLog(u"rgbColorFieldUpdated called.")
		self.debugLog(u"typeId: " + typeId + "\ndevId: " + str(devId) + "\nvaluesDict: " + str(valuesDict))
		valuesDict['rgbColor'] = self.calcRgbHexValsFromRgbLevels(valuesDict)

		# Can send a live update to the hardware here:
		#    self.sendSetRGBWCommand(valuesDict, typeId, devId)

		del valuesDict['red']
		del valuesDict['green']
		del valuesDict['blue']
		return (valuesDict)

	def hsbColorFieldUpdated(self, valuesDict, typeId, devId):
		self.debugLog(u"hsbColorFieldUpdated called.")
		self.debugLog(u"typeId: " + typeId + "\ndevId: " + str(devId) + "\nvaluesDict: " + str(valuesDict))
		valuesDict['rgbColor'] = self.calcRgbHexValsFromHsbLevels(valuesDict)

		# Can send a live update to the hardware here:
		#    self.sendSetRGBWCommand(valuesDict, typeId, devId)

		del valuesDict['hue']
		del valuesDict['saturation']
		del valuesDict['brightness']
		return (valuesDict)


	# Validate Device Configuration
	########################################
	def validateDeviceConfigUi(self, valuesDict, typeId, deviceId):
		self.debugLog(u"validateDeviceConfigUi called.\n  valuesDict: %s\n  typeId: %s\n  deviceId: %s" % (valuesDict, typeId, deviceId))
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = ""
		isError = False

		# Is this configuration for a hub?
		if typeId == "hueHub":

			# Validate the IP Address field.
			if valuesDict.get('address', "") == "":
				# The field was left blank.
				self.debugLog(u"IP address \"%s\" is blank." % valuesDict['address'])
				isError = True
				errorsDict['address'] = u"The IP Address field is blank. Please enter an IP Address for the Hue hub."
				errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

			else:
				# The field wasn't blank. Check to see if the format is valid.
				try:
					# Try to format the IP Address as a 32-bit binary value. If this fails, the format was invalid.
					self.debugLog(u"Validating IP address \"%s\"." % valuesDict['address'])
					socket.inet_aton(valuesDict['address'])

				except socket.error:
					# IP Address format was invalid.
					self.debugLog(u"IP address format is invalid.")
					isError = True
					errorsDict['address'] = u"The IP Address is not valid. Please enter a valid IP address."
					errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

			# If there haven't been any errors so far, try to connect to the Hue hub to see
			#   if it's actually a Hue hub.
			if not isError:
				try:
					self.debugLog(
						u"Verifying that a Hue hub exists at IP address \"%s\"." % valuesDict['address'])
					command = "http://%s/description.xml" % valuesDict['address']
					self.debugLog(u"Accessing URL: %s" % command)
					r = requests.get(command, timeout=kTimeout)
					self.debugLog(u"Got response:\n%s" % r.content)

					# Quick and dirty check to see if this is a Philips Hue hub.
					if "Philips hue bridge" not in r.content:
						# If "Philips hue bridge" doesn't exist in the response, it's not a Hue hub.
						self.debugLog(
							u"No \"Philips hue bridge\" string found in response. This isn't a Hue hub.")
						isError = True
						errorsDict[
							'address'] = u"This doesn't appear to be a Philips Hue hub.  Please verify the IP address."
						errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

					else:
						# This is likely a Hue hub.
						self.debugLog(u"Verified that this is a Hue hub.")

				except requests.exceptions.Timeout:
					self.debugLog(
						u"Connection to %s timed out after %i seconds." % (valuesDict['address'], kTimeout))
					isError = True
					errorsDict[
						'address'] = u"Unable to reach the hub. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
					errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

				except requests.exceptions.ConnectionError:
					self.debugLog(
						u"Connection to %s failed. There was a connection error." % valuesDict['address'])
					isError = True
					errorsDict[
						'address'] = u"Connection error. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
					errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

				except Exception, e:
					self.debugLog(u"Connection error. " + str(e))
					isError = True
					errorsDict[
						'address'] = u"Connection error. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
					errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

			# Successful
			return (True, valuesDict)

		# Otherwise, get our hub device
		hubId = valuesDict.get("hubId", None)
		hubDevice = None
		if hubId is not None and hubId != "":
			hubDevice = indigo.devices.get(int(hubId), None)
		else:
			errorsDict['hubId'] = u"Select a hub"
			return (False, valuesDict)

		# Make sure we're still paired with the Hue hub.
		if hubDevice is None or hubDevice.pluginProps.get("paired", False) == False:
			isError = True
			errorsDict['bulbId'] = u"Not currently paired with the Hue hub. Select a valid hub, and ensure it is paired first"
			errorsDict['showAlertText'] += errorsDict['bulbId']
			return (False, valuesDict, errorsDict)

		# Check data based on which device config UI was returned.
		#  -- Hue Bulb --
		if typeId == "hueBulb":
			# Make sure a bulb was selected.
			if valuesDict.get('bulbId', "") == "":
				isError = True
				errorsDict['bulbId'] = u"Please select a Hue Color/Ambiance light to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			bulbId = valuesDict['bulbId']

			# Make sure the device selected is a Hue device.
			#   Get the device info directly from the hub.
			command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Data from hub: " + r.content)
			# Convert the response to a Python object.
			try:
				bulb = json.loads(r.content)
			except Exception, e:
				# There was an error in the returned data.
				indigo.server.log(u"Error retrieving Hue device data from hub.  Error reported: " + str(e))
				isError = True
				errorsDict['bulbId'] = u"Error retrieving Hue device data from hub. See Indigo log."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)
			if bulb.get('modelid', "") not in kHueBulbDeviceIDs:
				isError = True
				errorsDict['bulbId'] = u"The selected device is not a Hue Color/Ambiance light. Plesea select a Hue Color/Ambiance light to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			# Make sure the bulb ID isn't used by another device.
			for otherDeviceId in self.deviceList:
				if otherDeviceId != deviceId:
					otherDevice = indigo.devices[otherDeviceId]
					if valuesDict['bulbId'] == otherDevice.pluginProps.get('bulbId', 0) and otherDevice.pluginProps.get("hubId", None) == hubId:
						otherDevice = indigo.devices[otherDeviceId]
						isError = True
						errorsDict['bulbId'] = u"This Hue device is already being controlled by the \"" + otherDevice.name + "\" Indigo device. Choose a different Hue bulb to control."
						errorsDict['showAlertText'] += errorsDict['bulbId'] + "\n\n"

			# Validate the default brightness is reasonable.
			if valuesDict.get('defaultBrightness', "") != "":
				try:
					defaultBrightness = int(valuesDict['defaultBrightness'])
					if defaultBrightness < 1 or defaultBrightness > 100:
						isError = True
						errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				valuesDict['address'] = hubDevice.pluginProps.get('address', "") + " (ID " + str(valuesDict['bulbId']) + ")"
				return (True, valuesDict)

		#  -- Ambiance Lights --
		if typeId == "hueAmbiance":
			# Make sure a bulb was selected.
			if valuesDict.get('bulbId', "") == "":
				isError = True
				errorsDict['bulbId'] = u"Please select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			bulbId = valuesDict['bulbId']

			# Make sure the device selected is a Hue device.
			#   Get the device info directly from the hub.
			command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Data from hub: " + r.content)
			# Convert the response to a Python object.
			try:
				bulb = json.loads(r.content)
			except Exception, e:
				# There was an error in the returned data.
				indigo.server.log(u"Error retrieving Hue device data from hub.  Error reported: " + str(e))
				isError = True
				errorsDict['bulbId'] = u"Error retrieving Hue device data from hub. See Indigo log."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)
			if bulb.get('modelid', "") not in kAmbianceDeviceIDs:
				isError = True
				errorsDict['bulbId'] = u"The selected device is not an Ambiance light. Please select an Ambiance light to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			# Make sure the bulb ID isn't used by another device.
			for otherDeviceId in self.deviceList:
				if otherDeviceId != deviceId:
					otherDevice = indigo.devices[otherDeviceId]
					if valuesDict['bulbId'] == otherDevice.pluginProps.get('bulbId', 0) and otherDevice.pluginProps.get(
						"hubId", None) == hubId:
						otherDevice = indigo.devices[otherDeviceId]
						isError = True
						errorsDict['bulbId'] = u"This Hue device is already being controlled by the \"" + otherDevice.name + "\" Indigo device. Choose a different Hue device to control."
						errorsDict['showAlertText'] += errorsDict['bulbId'] + "\n\n"

			# Validate the default brightness is reasonable.
			if valuesDict.get('defaultBrightness', "") != "":
				try:
					defaultBrightness = int(valuesDict['defaultBrightness'])
					if defaultBrightness < 1 or defaultBrightness > 100:
						isError = True
						errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				valuesDict['address'] = self.pluginPrefs.get('address', "") + " (ID " + str(valuesDict['bulbId']) + ")"
				return (True, valuesDict)

		#  -- LightStrips Device --
		elif typeId == "hueLightStrips":
			# Make sure a device was selected.
			if valuesDict.get('bulbId', "") == "":
				isError = True
				errorsDict['bulbId'] = u"Please select a LightStrips device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			bulbId = valuesDict['bulbId']

			# Make sure the device selected is a LightStrips device.
			#   Get the device info directly from the hub.
			command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Data from hub: " + r.content)
			# Convert the response to a Python object.
			try:
				bulb = json.loads(r.content)
			except Exception, e:
				# There was an error in the returned data.
				indigo.server.log(u"Error retrieving LightStrip data from hub.  Error reported: " + str(e))
				isError = True
				errorsDict['bulbId'] = u"Error retrieving LightStrip data from hub. See Indigo log."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)
			# Make sure it's a LightStrip device.
			if bulb.get('modelid', "") not in kLightStripsDeviceIDs:
				isError = True
				errorsDict['bulbId'] = u"The selected device is not a LightStrip device. Plesea select a LightStrip device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)
			# If it's an original LightStrip (not a new Plus version),
			#   remove the color temperature capabilities from the Indigo device.
			if bulb.get('modelid', "") == "LST001":
				self.debugLog(u"LightStrip device doesn't support color temperature. Removing color temperature from Indigo device properties.")
				if 'SupportsWhite' in valuesDict:
					valuesDict['SupportsWhite'] = False
				if 'SupportsWhiteTemperature' in valuesDict:
					valuesDict['SupportsWhiteTemperature'] = False
				if 'SupportsRGBandWhiteSimultaneously' in valuesDict:
					valuesDict['SupportsRGBandWhiteSimultaneously'] = False

			# Make sure the bulb ID isn't used by another device.
			for otherDeviceId in self.deviceList:
				if otherDeviceId != deviceId:
					otherDevice = indigo.devices[otherDeviceId]
					if valuesDict['bulbId'] == otherDevice.pluginProps.get('bulbId', 0) and otherDevice.pluginProps.get(
						"hubId", None) == hubId:
						otherDevice = indigo.devices[otherDeviceId]
						isError = True
						errorsDict['bulbId'] = u"This LightStrip device is already being controlled by the \"" + otherDevice.name + "\" Indigo device. Choose a different device to control."
						errorsDict['showAlertText'] += errorsDict['bulbId'] + "\n\n"

			# Validate the default brightness is reasonable.
			if valuesDict.get('defaultBrightness', "") != "":
				try:
					defaultBrightness = int(valuesDict['defaultBrightness'])
					if defaultBrightness < 1 or defaultBrightness > 100:
						isError = True
						errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				valuesDict['address'] = self.pluginPrefs.get('address', "") + " (ID " + str(valuesDict['bulbId']) + ")"
				return (True, valuesDict)

		#  -- LivingColors Bloom Device --
		elif typeId == "hueLivingColorsBloom":
			# Make sure a device was selected.
			if valuesDict.get('bulbId', "") == "":
				isError = True
				errorsDict['bulbId'] = u"Please select a LivingColors Bloom device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			bulbId = valuesDict['bulbId']

			# Make sure the device selected is a LivingColors device.
			#   Get the device info directly from the hub.
			command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Data from hub: " + r.content)
			# Convert the response to a Python object.
			try:
				bulb = json.loads(r.content)
			except Exception, e:
				# There was an error in the returned data.
				indigo.server.log(u"Error retrieving LovingColors Bloom data from hub.  Error reported: " + str(e))
				isError = True
				errorsDict['bulbId'] = u"Error retrieving LivingColors Bloom data from hub. See Indigo log."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)
			if bulb.get('modelid', "") not in kLivingColorsDeviceIDs:
				isError = True
				errorsDict['bulbId'] = u"The selected device is not a LivingColors Bloom device. Plesea select a LivingColors Bloom device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			# Make sure the bulb ID isn't used by another device.
			for otherDeviceId in self.deviceList:
				if otherDeviceId != deviceId:
					otherDevice = indigo.devices[otherDeviceId]
					if valuesDict['bulbId'] == otherDevice.pluginProps.get('bulbId', 0) and otherDevice.pluginProps.get(
						"hubId", None) == hubId:
						otherDevice = indigo.devices[otherDeviceId]
						isError = True
						errorsDict['bulbId'] = u"This LivingColors Bloom device is already being controlled by the \"" + otherDevice.name + "\" Indigo device. Choose a different device to control."
						errorsDict['showAlertText'] += errorsDict['bulbId'] + "\n\n"

			# Validate the default brightness is reasonable.
			if valuesDict.get('defaultBrightness', "") != "":
				try:
					defaultBrightness = int(valuesDict['defaultBrightness'])
					if defaultBrightness < 1 or defaultBrightness > 100:
						isError = True
						errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				valuesDict['address'] = self.pluginPrefs.get('address', "") + " (ID " + str(valuesDict['bulbId']) + ")"
				return (True, valuesDict)

		#  -- LivingWhites Device --
		elif typeId == "hueLivingWhites":
			# Make sure a device was selected.
			if valuesDict.get('bulbId', "") == "":
				isError = True
				errorsDict['bulbId'] = u"Please select a LivingWhites device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			bulbId = valuesDict['bulbId']

			# Make sure the device selected is a LightStrips device.
			#   Get the device info directly from the hub.
			command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Data from hub: " + r.content)
			# Convert the response to a Python object.
			try:
				bulb = json.loads(r.content)
			except Exception, e:
				# There was an error in the returned data.
				indigo.server.log(u"Error retrieving LivingWhites data from hub.  Error reported: " + str(e))
				isError = True
				errorsDict['bulbId'] = u"Error retrieving LivingWhites data from hub. See Indigo log."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)
			if bulb.get('modelid', "") not in kLivingWhitesDeviceIDs:
				isError = True
				errorsDict['bulbId'] = u"The selected device is not a LivingWhites device. Please select a LightStrips device to control."
				errorsDict['showAlertText'] += errorsDict['bulbId']
				return (False, valuesDict, errorsDict)

			# Make sure the bulb ID isn't used by another device.
			for otherDeviceId in self.deviceList:
				if otherDeviceId != deviceId:
					otherDevice = indigo.devices[otherDeviceId]
					if valuesDict['bulbId'] == otherDevice.pluginProps.get('bulbId', 0) and otherDevice.pluginProps.get(
						"hubId", None) == hubId:
						otherDevice = indigo.devices[otherDeviceId]
						isError = True
						errorsDict['bulbId'] = u"This LivingWhites device is already being controlled by the \"" + otherDevice.name + "\" Indigo device. Choose a different device to control."
						errorsDict['showAlertText'] += errorsDict['bulbId'] + "\n\n"

			# Validate the default brightness is reasonable.
			if valuesDict.get('defaultBrightness', "") != "":
				try:
					defaultBrightness = int(valuesDict['defaultBrightness'])
					if defaultBrightness < 1 or defaultBrightness > 100:
						isError = True
						errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				valuesDict['address'] = self.pluginPrefs.get('address', "") + " (ID " + str(valuesDict['bulbId']) + ")"
				return (True, valuesDict)

		#  -- Hue Group --
		if typeId == "hueGroup":
			# Make sure a group was selected.
			if valuesDict.get('groupId', "") == "":
				isError = True
				errorsDict['groupId'] = u"Please select a Hue Group to control."
				errorsDict['showAlertText'] += errorsDict['groupId']
				return (False, valuesDict, errorsDict)

			groupId = valuesDict['groupId']

			# Make sure the device selected is a Hue group.
			#   Get the group info directly from the hub.
			command = "http://%s/api/%s/groups/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Data from hub: " + r.content)
			# Convert the response to a Python object.
			try:
				group = json.loads(r.content)
			except Exception, e:
				# There was an error in the returned data.
				indigo.server.log(u"Error retrieving Hue group data from hub.  Error reported: " + str(e))
				isError = True
				errorsDict['groupId'] = u"Error retrieving Hue group data from hub. See Indigo log."
				errorsDict['showAlertText'] += errorsDict['groupId']
				return (False, valuesDict, errorsDict)
			if group.get('lights', "") == "":
				isError = True
				errorsDict['groupId'] = u"The selected item is not a Hue Group. Please select a Hue Group to control."
				errorsDict['showAlertText'] += errorsDict['groupId']
				return (False, valuesDict, errorsDict)

			# Make sure the group ID isn't used by another device.
			for otherDeviceId in self.deviceList:
				if otherDeviceId != deviceId:
					otherDevice = indigo.devices[otherDeviceId]
					if valuesDict['bulbId'] == otherDevice.pluginProps.get('bulbId', 0) and otherDevice.pluginProps.get(
						"hubId", None) == hubId:
						otherDevice = indigo.devices[otherDeviceId]
						isError = True
						errorsDict['groupId'] = u"This Hue group is already being controlled by the \"" + otherDevice.name + "\" Indigo device. Choose a different Hue group to control."
						errorsDict['showAlertText'] += errorsDict['groupId'] + "\n\n"

			# Validate the default brightness is reasonable.
			if valuesDict.get('defaultBrightness', "") != "":
				try:
					defaultBrightness = int(valuesDict['defaultBrightness'])
					if defaultBrightness < 1 or defaultBrightness > 100:
						isError = True
						errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['defaultBrightness'] = u"The Default Brightness must be a number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultBrightness'] + "\n\n"

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				valuesDict['address'] = self.pluginPrefs.get('address', "") + " (GID " + str(valuesDict['groupId']) + ")"
				return (True, valuesDict)

		# -- Hue Device Attribute Controller (Virtual Dimmer Device) --
		elif typeId == "hueAttributeController":
			# Make sure a Hue device was selected.
			if valuesDict.get('bulbDeviceId', "") == "":
				isError = True
				errorsDict['bulbDeviceId'] = u"Please select a Hue device whose attribute will be controlled."
				errorsDict['showAlertText'] += errorsDict['bulbDeviceId']

			# Make sure an Attribute to Control is selected.
			if valuesDict.get('attributeToControl', "") == "":
				isError = True
				errorsDict['attributeToControl'] = u"Please select an Attribute to Control."
				errorsDict['showAlertText'] += errorsDict['attributeToControl']

			# Validate the default ramp rate (transition time) is reasonable.
			if valuesDict.get('rate', "") != "":
				try:
					rampRate = float(valuesDict['rate'])
					if rampRate < 0 or rampRate > 540:
						isError = True
						errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				except Execption, e:
					isError = True
					errorsDict['rate'] = u"The Ramp Rate must be a number between 0 and 540 in increments of 0.1 seconds. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"

			# Validate the default on level.
			if valuesDict.get('defaultOnLevel', "") != "":
				try:
					onLevel = int(valuesDict['defaultOnLevel'])
					if onLevel < 1 or onLevel > 100:
						isError = True
						errorsDict['defaultOnLevel'] = u"The Default On Level must be a whole number between 1 and 100."
						errorsDict['showAlertText'] += errorsDict['defaultOnLevel'] + "\n\n"
				except ValueError:
					isError = True
					errorsDict['defaultOnLevel'] = u"The Default On Level must be a whole number between 1 and 100."
					errorsDict['showAlertText'] += errorsDict['defaultOnLevel'] + "\n\n"
				except Execption, e:
					isError = True
					errorsDict['defaultOnLevel'] = u"The Default On Level must be a whole number between 1 and 100. Error: " + str(e)
					errorsDict['showAlertText'] += errorsDict['defaultOnLevel'] + "\n\n"

			# Show errors if there are any.
			if isError:
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (False, valuesDict, errorsDict)

			else:
				# Define the device's address to appear in Indigo.
				# The address is the destination Hue device's device ID plus the attribute to control.
				device = indigo.devices[int(valuesDict.get('bulbDeviceId', 0))]
				valuesDict['address'] = str(device.id) + u" (" + valuesDict['attributeToControl'] + u")"
				return (True, valuesDict)

	# Validate Action Configuration.
	########################################
	def validateActionConfigUi(self, valuesDict, typeId, deviceId):

		if deviceId is not None and deviceId > 0:
			device = indigo.devices[deviceId]
			modelId = device.pluginProps.get('modelId', False)
			self.debugLog(u"Validating action config for type: " + typeId + u", device: " + device.name)
		else:
			device = None
			self.debugLog(u"Validating action config for type: " + typeId)

		self.debugLog(u"Values:\n" + str(valuesDict))
		isError = False
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = ""
		descString = u""


		### RECALL HUE SCENE
		if typeId == "recallScene":
			sceneId = valuesDict.get("sceneId", None)
			if sceneId is None:
				isError = True
				errorsDict['sceneId'] = u"Select a scene to recall"
				errorsDict['showAlertText'] += errorsDict['sceneId'] + "\n\n"


		### SET BRIGHTNESS WITH RAMP RATE ###
		elif typeId == "setBrightness":
			brightnessSource = valuesDict.get('brightnessSource', False)
			brightness = valuesDict.get('brightness', False)
			brightnessVarId = valuesDict.get('brightnessVariable', False)
			brightnessDevId = valuesDict.get('brightnessDevice', False)
			useRateVariable = valuesDict.get('useRateVariable', False)
			rate = valuesDict.get('rate', False)
			rateVarId = valuesDict.get('rateVariable', False)

			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			elif not brightnessSource:
				isError = True
				errorsDict['brightnessSource'] = u"Please specify a Brightness Source."
				errorsDict['showAlertText'] += errorsDict['brightnessSource'] + "\n\n"
			elif brightnessSource == "custom":
				if not brightness:
					isError = True
					errorsDict['brightness'] = u"Please specify a brightness level."
					errorsDict['showAlertText'] += errorsDict['brightness'] + "\n\n"
				else:
					try:
						brightness = int(brightness)
						if brightness < 0 or brightness > 100:
							isError = True
							errorsDict['brightness'] = u"Brightness levels must be a number between 0 and 100."
							errorsDict['showAlertText'] += errorsDict['brightness'] + "\n\n"
					except ValueError:
						isError = True
						errorsDict['brightness'] = u"Brightness levels must be a number between 0 and 100."
						errorsDict['showAlertText'] += errorsDict['brightness'] + "\n\n"
				descString += u"set brightness of \"" + device.name + "\" to " + str(brightness) + "%"
			elif brightnessSource == "variable":
				if not brightnessVarId:
					isError = True
					errorsDict['brightnessVariable'] = u"Please specify a variable to use for brightness level."
					errorsDict['showAlertText'] += errorsDict['brightnessVariable'] + "\n\n"
				else:
					try:
						brightnessVar = indigo.variables[int(brightnessVarId)]
						descString += u"set brightness of \"" + device.name + "\" to value in variable \"" + brightnessVar.name + "\""
					except IndexError:
						isError = True
						errorsDict['brightnessVariable'] = u"The specified variable does not exist in the Indigo database. Please choose a different variable."
						errorsDict['showAlertText'] += errorsDict['brightnessVariable'] + "\n\n"
			elif brightnessSource == "dimmer":
				if not brightnessDevId:
					isError = True
					errorsDict['brightnessDevice'] = u"Please specify a dimmer device to use as the source for brightness level."
					errorsDict['showAlertText'] += errorsDict['brightnessDevice'] + "\n\n"
				else:
					try:
						brightnessDev = indigo.devices[int(brightnessDevId)]
						descString += u"set brightness of \"" + device.name + "\" to current brightness of \"" + brightnessDev.name + "\""
					except IndexError:
						isError = True
						errorsDict['brightnessDevice'] = u"The specified device does not exist in the Indigo database. Please choose a different device."
						errorsDict['showAlertText'] += errorsDict['brightnessDevice'] + "\n\n"
					if brightnessDev.id == device.id:
						isError = True
						errorsDict['brightnessDevice'] = u"You cannot select the same dimmer as the one for which you're setting the brightness."
						errorsDict['showAlertText'] += errorsDict['brightnessDevice'] + "\n\n"

			if not useRateVariable:
				if not rate and rate.__class__ != bool:
					isError = True
					errorsDict['rate'] = u"Please enter a Ramp Rate."
					errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				else:
					try:
						rate = round(float(rate), 1)
						if rate < 0 or rate > 540:
							isError = True
							errorsDict['rate'] = u"Ramp Rate times must be between 0 and 540 seconds."
							errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
					except ValueError:
						isError = True
						errorsDict['rate'] = u"Ramp Rates must be between 0 and 540 seconds and cannot contain non-numeric characters."
						errorsDict['showAlertText'] += errorsDict['rate'] + "\n\n"
				descString += u" using ramp rate " + str(rate) + " sec"
			else:
				if not rateVarId:
					isError = True
					errorsDict['rateVariable'] = u"Please select a variable to use for the ramp rate."
					errorsDict['showAlertText'] += errorsDict['rateVariable'] + "\n\n"
				else:
					try:
						rateVar = indigo.variables[int(rateVarId)]
						descString += u" using ramp rate in variable \"" + rateVar.name + "\""
					except IndexError:
						isError = True
						errorsDict['rateVariable'] = u"The specified variable does not exist in the Indigo database. Please choose a different variable."
						errorsDict['showAlertText'] += errorsDict['rateVariable'] + "\n\n"

		### SET RGB LEVELS ###
		elif typeId == "setRGB":
			# Check the RGB values.
			red = valuesDict.get('red', 0)
			if red == "":
				red = 0
				valuesDict['red'] = red
			green = valuesDict.get('green', 0)
			if green == "":
				green = 0
				valuesDict['green'] = green
			blue = valuesDict.get('blue', 0)
			if blue == "":
				blue = 0
				valuesDict['blue'] = blue
			useRateVariable = valuesDict.get('useRateVariable', False)
			rateVariable = valuesDict.get('rateVariable', "")
			rampRate = valuesDict.get('rate', "")

			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle color.
			elif modelId not in kHueBulbDeviceIDs and modelId not in kLightStripsDeviceIDs and modelId not in kLivingColorsDeviceIDs and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device does not support color. Choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Validate red value.
			try:
				red = int(red)
				if (red < 0) or (red > 255):
					isError = True
					errorsDict['red'] = "Red values must be a whole number between 0 and 255."
					errorsDict['showAlertText'] += errorsDict['red'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['red'] = "Red values must be a whole number between 0 and 255."
				errorsDict['showAlertText'] += errorsDict['red'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['red'] = "Invalid Red value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['red'] + "\n\n"

			# Validate green value.
			try:
				green = int(green)
				if (green < 0) or (green > 255):
					isError = True
					errorsDict['green'] = "Green values must be a whole number between 0 and 255."
					errorsDict['showAlertText'] += errorsDict['green'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['green'] = "Green values must be a whole number between 0 and 255."
				errorsDict['showAlertText'] += errorsDict['green'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['green'] = "Invalid Green value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['green'] + "\n\n"

			# Validate blue value.
			try:
				blue = int(blue)
				if (blue < 0) or (blue > 255):
					isError = True
					errorsDict['blue'] = "Blue values must be a whole number between 0 and 255."
					errorsDict['showAlertText'] += errorsDict['blue'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['blue'] = "Blue values must be a whole number between 0 and 255."
				errorsDict['showAlertText'] += errorsDict['blue'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['blue'] = "Invalid Blue value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['blue'] + "\n\n"

			# Validate Ramp Rate.
			if not useRateVariable:
				# User entered a ramp rate value.
				if len(rampRate) > 0:
					try:
						rampRate = float(rampRate)
						if (rampRate < 0) or (rampRate > 540):
							isError = True
							errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
							errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except ValueError:
						isError = True
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except Exception, e:
						isError = True
						errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
			else:
				# User specified that they'd select a variable as the ramp rate source.
				# Make sure they actually selected one.
				if rateVariable == "":
					isError = True
					errorsDict['rateVariable'] = u"No variable was selected. Please select an Indigo variable as the ramp rate source."
					errorsDict['showAlertText'] += errorsDict['rateVariable'] + u"\n\n"
				else:
					# Since a variable ID was given, convert it to an integer.
					rateVariable = int(rateVariable)

			if not isError:
				descString += u"set hue device RGB levels to " + str(red) + ", " + str(green) + ", " + str(blue)
				if useRateVariable == True:
					descString += u" using ramp rate in variable \"" + indigo.variables[rateVariable].name + u"\"."
				else:
					if len(valuesDict.get('rate', "")) > 0:
						descString += u" with ramp rate " + str(rampRate) + u" sec"

		### SET HSB ###
		elif typeId == "setHSB":
			# Check the HSB values.
			hue = valuesDict.get('hue', 0)
			if hue == "":
				hue = 0
				valuesDict['hue'] = hue
			saturation = valuesDict.get('saturation', 100)
			if saturation == "":
				saturation = 100
				valuesDict['saturation'] = saturation
			brightnessSource = valuesDict.get('brightnessSource', "custom")
			brightnessVariable = valuesDict.get('brightnessVariable', "")
			brightnessDevice = valuesDict.get('brightnessDevice', "")
			if brightnessSource == "":
				brightnessSource = "custom"
				valuesDict['brightnessSource'] = brightnessSource
			brightness = valuesDict.get('brightness', "")
			if brightness == "":
				brightness = device.states['brightnessLevel']
				valuesDict['brightness'] = brightness
			useRateVariable = valuesDict.get('useRateVariable', False)
			rateVariable = valuesDict.get('rateVariable', "")
			rampRate = valuesDict.get('rate', "")

			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle color.
			elif modelId not in kHueBulbDeviceIDs and modelId not in kLightStripsDeviceIDs and modelId not in kLivingColorsDeviceIDs and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device does not support color. Choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Validate hue value.
			try:
				hue = int(hue)
				if (hue < 0) or (hue > 360):
					isError = True
					errorsDict['hue'] = "Hue values must be a whole number between 0 and 360 degrees."
					errorsDict['showAlertText'] += errorsDict['hue'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['hue'] = "Hue values must be a whole number between 0 and 360 degrees."
				errorsDict['showAlertText'] += errorsDict['hue'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['hue'] = "Invalid Hue value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['hue'] + "\n\n"

			# Validate saturation value.
			try:
				saturation = int(saturation)
				if (saturation < 0) or (saturation > 100):
					isError = True
					errorsDict['saturation'] = "Saturation values must be a whole number between 0 and 100 percent."
					errorsDict['showAlertText'] += errorsDict['saturation'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['saturation'] = "Saturation values must be a whole number between 0 and 100 percent."
				errorsDict['showAlertText'] += errorsDict['saturation'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['saturation'] = "Invalid Saturation value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['saturation'] + "\n\n"

			# Validate the brightness value.
			if brightnessSource == "custom":
				try:
					brightness = int(brightness)
					if (brightness < 0) or (brightness > 100):
						isError = True
						errorsDict['brightness'] = u"Brightness values must be a whole number between 0 and 100 percent."
						errorsDict['showAlertText'] += errorsDict['brightness'] + u"\n\n"
				except ValueError:
					isError = True
					errorsDict['brightness'] = u"Brightness values must be a whole number between 0 and 100 percent."
					errorsDict['showAlertText'] += errorsDict['brightness'] + u"\n\n"
				except Exception, e:
					isError = True
					errorsDict['brightness'] = u"Invalid Brightness value: " + str(e)
					errorsDict['showAlertText'] += errorsDict['brightness'] + u"\n\n"
			elif brightnessSource == "variable":
				# Make sure the variable selection is valid.
				if brightnessVariable == "":
					isError = True
					errorsDict['brightnessVariable'] = u"No source variable selected. Please select an Indigo variable from the list."
					errorsDict['showAlertText'] += errorsDict['brightnessVariable'] + u"\n\n"
				else:
					# Since a variable ID was given, convert it to an integer.
					brightnessVariable = int(brightnessVariable)
			elif brightnessSource == "dimmer":
				# Make sure the device selection is valid.
				if brightnessDevice == "":
					isError = True
					errorsDict['brightnessDevice'] = u"No source device selected. Please select an Indigo dimmer device from the list."
					errorsDict['showAlertText'] += errorsDict['brightnessDevice'] + u"\n\n"
				else:
					# Since a device ID was given, convert it to an integer.
					brightnessDevice = int(brightnessDevice)

			# Validate Ramp Rate.
			if not useRateVariable:
				# User entered a ramp rate value.
				if len(rampRate) > 0:
					try:
						rampRate = float(rampRate)
						if (rampRate < 0) or (rampRate > 540):
							isError = True
							errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
							errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except ValueError:
						isError = True
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except Exception, e:
						isError = True
						errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
			else:
				# User specified that they'd select a variable as the ramp rate source.
				# Make sure they actually selected one.
				if rateVariable == "":
					isError = True
					errorsDict['rateVariable'] = u"No variable was selected. Please select an Indigo variable as the ramp rate source."
					errorsDict['showAlertText'] += errorsDict['rateVariable'] + u"\n\n"
				else:
					# Since a variable ID was given, convert it to an integer.
					rateVariable = int(rateVariable)

			if not isError:
				descString += u"set hue device hue to " + str(hue) + u", saturation to " + str(saturation) + u" and brightness to"
				if brightnessSource == "custom":
					descString += str(brightness)
				elif brightnessSource == "variable":
					descString += u" value in variable \"" + indigo.variables[brightnessVariable].name + u"\""
				elif brightnessSource == "dimmer":
					descString += u" brightness of device \"" + indigo.devices[brightnessDevice].name + u"\""

				if useRateVariable == True:
					descString += u" using ramp rate in variable \"" + indigo.variables[rateVariable].name + u"\"."
				else:
					if len(valuesDict.get('rate', "")) > 0:
						descString += u" with ramp rate " + str(rampRate) + u" sec"

		### SET xyY ###
		elif typeId == "setXYY":
			# Check the xyY values.
			colorX = valuesDict.get('xyy_x', 0)
			if colorX == "":
				colorX = 0
				valuesDict['xyy_x'] = colorX
			colorY = valuesDict.get('xyy_y', 0)
			if colorY == "":
				colorY = 0
				valuesDict['xyy_y'] = colorY
			brightness = valuesDict.get('xyy_Y', 0)
			if brightness == "":
				brightness = float(device.states['brightnessLevel']) / 100.0
				valuesDict['xyy_Y'] = brightness
			useRateVariable = valuesDict.get('useRateVariable', False)
			rateVariable = valuesDict.get('rateVariable', "")
			rampRate = valuesDict.get('rate', "")

			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle color.
			elif modelId not in kHueBulbDeviceIDs and modelId not in kLightStripsDeviceIDs and modelId not in kLivingColorsDeviceIDs and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device does not support color. Choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Validate x chromatisity value.
			try:
				colorX = float(colorX)
				if (colorX < 0) or (colorX > 1):
					isError = True
					errorsDict['xyy_x'] = "x Chromatisety values must be a number between 0 and 1.0."
					errorsDict['showAlertText'] += errorsDict['xyy_x'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['xyy_x'] = "x Chromatisety values must be a number between 0 and 1.0."
				errorsDict['showAlertText'] += errorsDict['xyy_x'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['xyy_x'] = "Invalid x Chromatisety value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['xyy_x'] + "\n\n"

			# Validate y chromatisity value.
			try:
				colorY = float(colorY)
				if (colorY < 0) or (colorY > 1):
					isError = True
					errorsDict['xyy_y'] = "y Chromatisety values must be a number between 0 and 1.0."
					errorsDict['showAlertText'] += errorsDict['xyy_y'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['xyy_y'] = "y Chromatisety values must be a number between 0 and 1.0."
				errorsDict['showAlertText'] += errorsDict['xyy_y'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['xyy_y'] = "Invalid y Chromatisety value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['xyy_y'] + "\n\n"

			# Validate Y luminosity value.
			try:
				brightness = float(brightness)
				if (brightness < 0) or (brightness > 1):
					isError = True
					errorsDict['xyy_Y'] = "Y Luminosity values must be a number between 0 and 1.0."
					errorsDict['showAlertText'] += errorsDict['xyy_Y'] + "\n\n"
			except ValueError:
				isError = True
				errorsDict['xyy_Y'] = "Y Luminosity values must be a number between 0 and 1.0."
				errorsDict['showAlertText'] += errorsDict['xyy_Y'] + "\n\n"
			except Exception, e:
				isError = True
				errorsDict['xyy_Y'] = "Invalid Y Luminosity value: " + str(e)
				errorsDict['showAlertText'] += errorsDict['xyy_Y'] + "\n\n"

			# Validate Ramp Rate.
			if not useRateVariable:
				# User entered a ramp rate value.
				if len(rampRate) > 0:
					try:
						rampRate = float(rampRate)
						if (rampRate < 0) or (rampRate > 540):
							isError = True
							errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
							errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except ValueError:
						isError = True
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except Exception, e:
						isError = True
						errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
			else:
				# User specified that they'd select a variable as the ramp rate source.
				# Make sure they actually selected one.
				if rateVariable == "":
					isError = True
					errorsDict['rateVariable'] = u"No variable was selected. Please select an Indigo variable as the ramp rate source."
					errorsDict['showAlertText'] += errorsDict['rateVariable'] + u"\n\n"
				else:
					# Since a variable ID was given, convert it to an integer.
					rateVariable = int(rateVariable)

			if not isError:
				descString += u"set hue device xyY chromatisety to " + str(colorX) + ", " + str(colorY) + ", " + str(brightness)
				if useRateVariable == True:
					descString += u" using ramp rate in variable \"" + indigo.variables[rateVariable].name + u"\"."
				else:
					if len(valuesDict.get('rate', "")) > 0:
						descString += u" with ramp rate " + str(rampRate) + u" sec"

		### SET COLOR TEMPERATURE ###
		elif typeId == "setCT":
			# Check the Color Temperature values.
			preset = valuesDict.get('preset', False)
			# The "preset" designation is referred to as a "color recipe" by Phillips.
			if preset == "":
				preset = "relax"	# The "relax" recipe is the first in the list, so use it as default.
				valuesDict['preset'] = preset
			temperatureSource = valuesDict.get('temperatureSource', "custom")
			temperatureVariable = valuesDict.get('temperatureVariable', "")
			if temperatureSource == "":
				temperatureSource = "custom"
				valuesDict['temperatureSource'] = temperatureSource
			temperature = valuesDict.get('temperature', "")
			if temperature == "":
				temperature = 2800
				valuesDict['temperature'] = temperature
			brightnessSource = valuesDict.get('brightnessSource', "custom")
			brightnessVariable = valuesDict.get('brightnessVariable', "")
			brightnessDevice = valuesDict.get('brightnessDevice', "")
			if brightnessSource == "":
				brightnessSource = "custom"
				valuesDict['brightnessSource'] = brightnessSource
			brightness = valuesDict.get('brightness', "")
			if brightness == "":
				brightness = device.states['brightnessLevel']
				valuesDict['brightness'] = brightness
			useRateVariable = valuesDict.get('useRateVariable', False)
			rateVariable = valuesDict.get('rateVariable', "")
			rampRate = valuesDict.get('rate', "")

			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle color temperature changes.
			elif modelId not in kHueBulbDeviceIDs and modelId not in kLightStripsDeviceIDs and modelId not in kAmbianceDeviceIDs and modelId != "LST001" and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device does not support variable color temperature. Choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Validate that a Preset Color Recipe item or Custom was selected.
			if preset == False:
				isError = True
				errorsDict['preset'] = u"Please select an item from the Preset Color Recipe menu."
				errorsDict['showAlertText'] += errorsDict['preset'] + u"\n\n"
			elif preset == "custom":
				# Custom temperature and brightness.
				# Validate the temperature value.
				if temperatureSource == "custom":
					try:
						temperature = int(temperature)
						if (temperature < 2000) or (temperature > 6500):
							isError = True
							errorsDict['temperature'] = u"Color Temperature values must be a whole number between 2000 and 6500 Kelvin."
							errorsDict['showAlertText'] += errorsDict['temperature'] + u"\n\n"
					except ValueError:
						isError = True
						errorsDict['temperature'] = u"Color Temperature values must be a whole number between 2000 and 6500 Kelvin."
						errorsDict['showAlertText'] += errorsDict['temperature'] + u"\n\n"
					except Exception, e:
						isError = True
						errorsDict['temperature'] = u"Invalid Color Temperature value: " + str(e)
						errorsDict['showAlertText'] += errorsDict['temperature'] + u"\n\n"
				elif temperatureSource == "variable":
					# Make sure the variable selection is valid.
					if temperatureVariable == "":
						isError = True
						errorsDict['temperatureVariable'] = u"No source variable selected. Please select an Indigo variable from the list."
						errorsDict['showAlertText'] += errorsDict['temperatureVariable'] + u"\n\n"
					else:
						# Since a variable ID was given, convert it to an integer.
						temperatureVariable = int(temperatureVariable)
				# Validate the brightness value.
				if brightnessSource == "custom":
					try:
						brightness = int(brightness)
						if (brightness < 0) or (brightness > 100):
							isError = True
							errorsDict['brightness'] = u"Brightness values must be a whole number between 0 and 100 percent."
							errorsDict['showAlertText'] += errorsDict['brightness'] + u"\n\n"
					except ValueError:
						isError = True
						errorsDict['brightness'] = u"Brightness values must be a whole number between 0 and 100 percent."
						errorsDict['showAlertText'] += errorsDict['brightness'] + u"\n\n"
					except Exception, e:
						isError = True
						errorsDict['brightness'] = u"Invalid Brightness value: " + str(e)
						errorsDict['showAlertText'] += errorsDict['brightness'] + u"\n\n"
				elif brightnessSource == "variable":
					# Make sure the variable selection is valid.
					if brightnessVariable == "":
						isError = True
						errorsDict['brightnessVariable'] = u"No source variable selected. Please select an Indigo variable from the list."
						errorsDict['showAlertText'] += errorsDict['brightnessVariable'] + u"\n\n"
					else:
						# Since a variable ID was given, convert it to an integer.
						brightnessVariable = int(brightnessVariable)
				elif brightnessSource == "dimmer":
					# Make sure the device selection is valid.
					if brightnessDevice == "":
						isError = True
						errorsDict['brightnessDevice'] = u"No source device selected. Please select an Indigo dimmer device from the list."
						errorsDict['showAlertText'] += errorsDict['brightnessDevice'] + u"\n\n"
					else:
						# Since a device ID was given, convert it to an integer.
						brightnessDevice = int(brightnessDevice)
			# Validate Ramp Rate.
			if not useRateVariable:
				# User entered a ramp rate value.
				if len(rampRate) > 0:
					try:
						rampRate = float(rampRate)
						if (rampRate < 0) or (rampRate > 540):
							isError = True
							errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
							errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except ValueError:
						isError = True
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
					except Exception, e:
						isError = True
						errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
			else:
				# User specified that they'd select a variable as the ramp rate source.
				# Make sure they actually selected one.
				if rateVariable == "":
					isError = True
					errorsDict['rateVariable'] = u"No variable was selected. Please select an Indigo variable as the ramp rate source."
					errorsDict['showAlertText'] += errorsDict['rateVariable'] + u"\n\n"
				else:
					# Since a variable ID was given, convert it to an integer.
					rateVariable = int(rateVariable)

			# If there were no errors...
			if not isError:
				descString += u"set hue device color temperature to"
				if preset != "custom":
					descString += u" preset color recipe \"" + preset + u"\""
				else:
					if temperatureSource == "custom":
						descString += u" custom value " + str(temperature) + u" K"
					elif temperatureSource == "variable":
						descString += u" value in variable \"" + indigo.variables[temperatureVariable].name + u"\""

					if brightnessSource == "custom":
						descString += u" at " + str(brightness) + u"% brightness"
					elif brightnessSource == "variable":
						descString += u" using brightness value in variable \"" + indigo.variables[brightnessVariable].name + u"\""
					elif brightnessSource == "dimmer":
						descString += u" using brightness of device \"" + indigo.devices[brightnessDevice].name + u"\""

				if useRateVariable == True:
					descString += u" using ramp rate in variable \"" + indigo.variables[rateVariable].name + u"\"."
				else:
					if len(valuesDict.get('rate', "")) > 0:
						descString += u" with ramp rate " + str(rampRate) + u" sec"

		### EFFECT ###
		elif typeId == "effect":
			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle the color effect.
			elif modelId not in kHueBulbDeviceIDs and modelId not in kLightStripsDeviceIDs and modelId not in kLivingColorsDeviceIDs and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device does not support color effects. Choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Make sure an effect was specified.
			effect = valuesDict.get('effect', "")
			if not effect:
				isError = True
				errorsDict['effect'] = u"No effect setting was selected."
				errorsDict['showAlertText'] += errorsDict['effect'] + u"\n\n"
			else:
				descString = u"set hue device effect to \"" + effect + u"\""

		### SAVE PRESET ###
		elif typeId == "savePreset":
			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle the color effect.
			elif modelId not in kCompatibleDeviceIDs and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device is not a compatible Hue device. Please choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Make sure the Preset Name isn't too long.
			if len(valuesDict.get('presetName', "")) > 50:
				isError = True
				errorsDict['presetName'] = u"The Preset Name is too long. Please use a name that is no more than 50 characters long."
				errorsDict['showAlertText'] += errorsDict['presetName'] + "\n\n"

			# Make sure a Preset was selected.
			presetId = valuesDict.get('presetId', "")
			if presetId == "":
				isError = True
				errorsDict['presetId'] = u"No Preset was selected."
				errorsDict['showAlertText'] += errorsDict['presetId'] + u"\n\n"
			else:
				descString = u"save hue device settings to preset " + str(presetId)

			# Validate Ramp Rate.
			rampRate = valuesDict.get('rate', "")
			if len(rampRate) > 0:
				try:
					rampRate = float(rampRate)
					if (rampRate < 0) or (rampRate > 540):
						isError = True
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"

		### RECALL PRESET ###
		elif typeId == "recallPreset":
			# First make sure this is a Hue device and not an attribute controller.
			if device.deviceTypeId == "hueAttributeController":
				isError = True
				errorsDict['device'] = u"This action cannot be applied to Hue Device Attribute Controllers. Please cancel the configuration dialog and select a Hue device to control."
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"
			# If it is a valid device, check everything else.
			# Make sure this device can handle the color effect.
			elif modelId not in kCompatibleDeviceIDs and device.deviceTypeId != "hueGroup":
				isError = True
				errorsDict['device'] = u"The \"%s\" device is not a compatible Hue device. Please choose a different device." % (device.name)
				errorsDict['showAlertText'] += errorsDict['device'] + "\n\n"

			# Make sure a Preset was selected.
			presetId = valuesDict.get('presetId', "")
			if presetId == "":
				isError = True
				errorsDict['presetId'] = u"No Preset was selected."
				errorsDict['showAlertText'] += errorsDict['presetId'] + u"\n\n"
			else:
				# Make sure the preset isn't empty.
				if len(self.pluginPrefs['presets'][int(presetId) - 1][1]) < 1:
					isError = True
					errorsDict['presetId'] = u"This Preset is empty. Please choose a Preset with data already saved to it (one with an asterisk (*) next to the number)."
					errorsDict['showAlertText'] += errorsDict['presetId'] + u"\n\n"
				else:
					descString = u"recall hue device settings from preset " + str(presetId)

			# Validate Ramp Rate.
			rampRate = valuesDict.get('rate', "")
			if len(rampRate) > 0:
				try:
					rampRate = float(rampRate)
					if (rampRate < 0) or (rampRate > 540):
						isError = True
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
				except ValueError:
					isError = True
					errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"
				except Exception, e:
					isError = True
					errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate'] + u"\n\n"

		### CATCH ALL ###
		else:
			isError = True
			errorsDict['presetId'] = u"The typeId \"" + str(typeId) + "\" wasn't recognized."
			errorsDict['showAlertText'] += errorsDict['presetId'] + u"\n\n"

		# Define the description value.
		valuesDict['description'] = descString
		# Return an error if one exists.
		if isError:
			errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
			return (False, valuesDict, errorsDict)

		return (True, valuesDict)

	# Validate Preferences Configuration.
	########################################
	def validatePrefsConfigUi(self, valuesDict):
		self.debugLog(u"Starting validatePrefsConfigUi.")
		self.debugLog(u"Values passed:\n%s" % valuesDict)
		isError = False
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = ""

		# Return an error if one exists.
		if isError:
			errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
			return (False, valuesDict, errorsDict)
		else:
			return (True, valuesDict)

	# Plugin Configuration Dialog Closed
	########################################
	def closedPrefsConfigUi(self, valuesDict, userCancelled):
		self.debugLog(u"Starting closedPrefsConfigUi.")

		# If the user didn't cancel the changes, take any needed actions as a result of the changes made.
		if not userCancelled:
			# Configuration was saved.

			# Update debug logging state.
			self.debug = valuesDict.get('showDebugInfo', False)
			# Make a note of what changed in the Indigo log.
			if self.debug:
				indigo.server.log(u"Debug logging enabled")
			else:
				indigo.server.log(u"Debug logging disabled")

	def deviceHubChanged(self, valuesDict, typeId, devId):
		self.debugLog("Selected hub for bulb device was changed")
		return (True, valuesDict)

	# Scene List Generator
	########################################
	def sceneListGenerator(self, filter="", valuesDict=None, typeId="", targetId=0):

		returnSceneList = list()

		# Get the hub ID
		hubId = targetId if targetId > 0 else valuesDict.get("hubId", None)
		if hubId is None:
			self.debugLog("Asked to get list of scenes without a hub. Refusing.")
			return returnSceneList

		# Get the hub
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get a hub with ID '%i'" % (hubId))
			return returnSceneList

		# Get the scenesDict for this hub
		hubScenesDict = self.scenesDict[str(hubId)]

		# Iterate over our scenes, and return the available list in Indigo's format
		for sceneId, sceneDetails in hubScenesDict.items():
			if sceneDetails.get("recycle", False) == False:
				returnSceneList.append([sceneId, sceneDetails["name"]])

		# Done
		return returnSceneList

	# Bulb List Generator
	########################################
	def bulbListGenerator(self, filter="", valuesDict=None, typeId="", targetId=0):
		returnBulbList = list()
		# Used in actions that need a list of Hue hub devices.
		self.debugLog(u"bulbListGenerator called.\n  filter: %s\n  valuesDict: %s\n  typeId: %s\n  targetId: %s" % (filter, valuesDict, typeId, targetId))

		# Get the hub ID
		hubId = valuesDict.get("hubId", None)
		if hubId is None:
			self.errorLog("Asked to get list of bulbs without a hub. Refusing.")
			return returnBulbList

		# Get the lightsDict for this hub
		hubLightsDict = self.lightsDict[str(hubId)]

		# Get the hub
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get a hub with ID '%i'" % (hubId))
			return returnBulbList

		# Iterate over our bulbs, and return the available list in Indigo's format
		for bulbId, bulbDetails in hubLightsDict.items():
			# First, get the device info directly from the hub (if the typeId is not blank).
			if typeId != "":
				command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
				self.debugLog(u"Sending URL request: " + command)
				try:
					r = requests.get(command, timeout=kTimeout)
				except requests.exceptions.Timeout:
					errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
					# Don't display the error if it's been displayed already.
					if errorText != self.lastErrorMessage:
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
				except requests.exceptions.ConnectionError:
					errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
					# Don't display the error if it's been displayed already.
					if errorText != self.lastErrorMessage:
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
				try:
					# If the content contains non-ASCII characters, this will fail.
					self.debugLog(u"Data from hub: " + r.content)
				except Exception, e:
					self.debugLog(u"Data from hub could not be displayed because of an error: " + str(e))
				# Convert the response to a Python object.
				try:
					bulb = json.loads(r.content)
				except Exception, e:
					# There was an error in the returned data.
					indigo.server.log(u"Error retrieving Hue bulb data from hub.  Error reported: " + str(e))


			# Next, limit the list to the type of devices indicated in the filter variable.
			if typeId == "":
				# If no typeId exists, list all devices.
				returnBulbList.append([bulbId, bulbDetails["name"]])
			elif typeId == "hueBulb" and bulb.get('modelid', "") in kHueBulbDeviceIDs:
				returnBulbList.append([bulbId, bulbDetails["name"]])
			elif typeId == "hueAmbiance" and bulb.get('modelid', "") in kAmbianceDeviceIDs:
				returnBulbList.append([bulbId, bulbDetails["name"]])
			elif typeId == "hueLightStrips" and bulb.get('modelid', "") in kLightStripsDeviceIDs:
				returnBulbList.append([bulbId, bulbDetails["name"]])
			elif typeId == "hueLivingColorsBloom" and bulb.get('modelid', "") in kLivingColorsDeviceIDs:
				returnBulbList.append([bulbId, bulbDetails["name"]])
			elif typeId == "hueLivingWhites" and bulb.get('modelid', "") in kLivingWhitesDeviceIDs:
				returnBulbList.append([bulbId, bulbDetails["name"]])

		# Debug
		self.debugLog(u"Return bulb list is %s" % returnBulbList)

		return returnBulbList

	# Group List Generator
	########################################
	def groupListGenerator(self, filter="", valuesDict=None, typeId="", targetId=0):
		returnGroupList = list()
		# Used in actions that need a list of Hue hub groups.
		self.debugLog(u"groupListGenerator called.\n  filter: %s\n  valuesDict: %s\n  typeId: %s\n  targetId: %s" % (filter, valuesDict, typeId, targetId))

		# Get the hub ID
		hubId = valuesDict.get("hubId", None)
		if hubId is None:
			self.errorLog("Asked to get list of groups without a hub. Refusing.")
			return returnGroupList

		# Get the lightsDict for this hub
		hubGroupsDict = self.groupsDict[str(hubId)]

		# Get the hub
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get a hub with ID '%i'" % (hubId))
			return returnGroupList

		# Add the special default zero group to the beginning of the list.
		returnGroupList.append([0, "0: (All Hue Devices)"])

		# Iterate over our groups, and return the available list in Indigo's format
		for groupId, groupDetails in sorted(hubGroupsDict.items()):
			# First, get the group info directly from the hub (if the typeId is not blank).
			if typeId != "":
				command = "http://%s/api/%s/groups/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
				self.debugLog(u"Sending URL request: " + command)
				try:
					r = requests.get(command, timeout=kTimeout)
				except requests.exceptions.Timeout:
					errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
					# Don't display the error if it's been displayed already.
					if errorText != self.lastErrorMessage:
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
				except requests.exceptions.ConnectionError:
					errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
					# Don't display the error if it's been displayed already.
					if errorText != self.lastErrorMessage:
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
				try:
					# If the content contains non-ASCII characters, this will fail.
					self.debugLog(u"Data from hub: " + r.content)
				except Exception, e:
					self.debugLog(u"Data from hub could not be displayed because of an error: " + str(e))
				# Convert the response to a Python object.
				try:
					group = json.loads(r.content)
				except Exception, e:
					# There was an error in the returned data.
					indigo.server.log(u"Error retrieving Hue group data from hub.  Error reported: " + str(e))

			returnGroupList.append([groupId, str(groupId) + ": " + groupDetails["name"]])

		# Debug
		self.debugLog(u"Return group list is %s" % returnGroupList)

		return returnGroupList

	# Bulb Device List Generator
	########################################
	def bulbDeviceListGenerator(self, filter="", valuesDict=None, typeId="", targetId=0):
		returnDeviceList = list()
		# Used in actions that need a list of Hue Lights plugin devices that aren't
		#   attribute controllers or groups.

		# Get the hub ID
		hubId = valuesDict.get("hubId", None)
		if hubId is None:
			self.errorLog("Asked to get list of bulbs without a hub. Refusing.")
			return returnDeviceList

		# Iterate over our devices, and return the available devices as a 2-tuple list.
		for deviceId in self.deviceList:
			device = indigo.devices[deviceId]
			if device.deviceTypeId != "hueAttributeController" and device.pluginProps.get("hubId", None) == hubId:
				returnDeviceList.append([deviceId, device.name])

		# Debug
		self.debugLog(u"Return Hue device list is %s" % returnDeviceList)

		return returnDeviceList

	# Generate Presets List
	########################################
	def presetListGenerator(self, filter="", valuesDict=None, typeId="", deviceId=0):
		self.debugLog(u"presetListGenerator called. typeId: " + str(typeId) + u", targetId: " + str(deviceId))

		theList = list()	# Menu item list.

		presets = self.pluginPrefs.get('presets', None)
		self.debugLog(u"Presets in plugin prefs:\n" + str(presets))

		if presets != None:
			presetNumber = 0

			for preset in presets:
				# Determine whether the Preset has saved data or not.
				hasData = ""
				if len(presets[presetNumber][1]) > 0:
					hasData = "*"

				presetNumber += 1
				presetName = preset[0]
				theList.append((presetNumber, hasData + str(presetNumber) + ": " + presetName))
		else:
			theList.append((0, "-- no presets --"))

		return theList

	# Did Device Communications Properties Change?
	########################################
	def didDeviceCommPropertyChange(self, origDev, newDev):
		# Automatically called by plugin host when device properties change.
		self.debugLog("didDeviceCommPropertyChange called.")
		# We only want to reload the device if the bulbId changes.
		if origDev.deviceTypeId != "hueAttributeController" and origDev.deviceTypeId != "hueGroup" and origDev.deviceTypeId != "hueHub":
			if origDev.pluginProps['bulbId'] != newDev.pluginProps['bulbId']:
				return True
			return False
		else:
			# This is some device type other than a Hue bulb, so do the
			#   default action of returning True if anything has changed.
			if origDev.pluginProps != newDev.pluginProps:
				return True
			return False


	########################################
	# Plugin-Specific Device Methods
	########################################

	# Update Device State
	########################################
	def updateDeviceState(self, device, state, newValue):
		# Change the device state on the server
		#   if it's different than the current state.

		# First, if the state doesn't even exist on the device, force a reload
		#   of the device configuration to try to add the new state.
		if device.states.get(state, None) is None:
			self.debugLog(u"The " + device.name + u" device doesn't have the \"" + state + u"\" state.  Updating device.")
			device.stateListOrDisplayStateIdChanged()

		# Now try to update the state.
		if (newValue != device.states.get(state, None)):
			try:
				self.debugLog(u"updateDeviceState: Updating device " + device.name + u" state: " + str(state) + u" = " + str(newValue))
			except Exception, e:
				self.debugLog(u"updateDeviceState: Updating device " + device.name + u" state: (Unable to display state due to error: " + str(e) + u")")
			# If this is a floating point number, specify the maximum
			#   number of digits to make visible in the state.  Everything
			#   in this plugin only needs 1 decimal place of precission.
			#   If this isn't a floating point value, don't specify a number
			#   of decimal places to display.
			if newValue.__class__ == float:
				device.updateStateOnServer(key=state, value=newValue, decimalPlaces=4)
			else:
				device.updateStateOnServer(key=state, value=newValue)

	# Update Device Properties
	########################################
	def updateDeviceProps(self, device, newProps):
		# Change the properties on the server only if there's actually been a change.
		if device.pluginProps != newProps:
			self.debugLog(u"updateDeviceProps: Updating device " + device.name + u" properties.")
			device.replacePluginPropsOnServer(newProps)


	########################################
	# Hue Communication Methods
	########################################

	# Get Bulb Status
	########################################
	def getBulbStatus(self, deviceId):
		# Get device status.

		device = indigo.devices[deviceId]
		self.debugLog(u"Get device status for " + device.name)
		# Proceed based on the device type.
		if device.deviceTypeId == "hueGroup":
			# This is a Hue Group device. Redirect the call to the group status update.
			self.getGroupStatus(deviceId)
			return
		else:

			# Get the hub from the device
			hubId = device.pluginProps.get("hubId", None)
			if hubId is None:
				self.errorLog("No hub for device '%s'" % (device.name))
				return
			hubDevice = indigo.devices.get(int(hubId), None)
			if hubDevice is None:
				self.errorLog("Failed to get hub for device '%s'" % (device.name))
				return

			# Get the bulbId from the device properties.
			bulbId = device.pluginProps.get('bulbId', False)
			# if the bulbId exists, get the device status.
			if bulbId:
				command = "http://%s/api/%s/lights/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
				self.debugLog(u"Sending URL request: " + command)
				try:
					r = requests.get(command, timeout=kTimeout)
				except requests.exceptions.Timeout:
					errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
					# Don't display the error if it's been displayed already.
					if errorText != self.lastErrorMessage:
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
					return
				except requests.exceptions.ConnectionError:
					errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
					# Don't display the error if it's been displayed already.
					if errorText != self.lastErrorMessage:
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
					return
			# The Indigo device
			#   must not yet be configured. Just return gracefully.
			else:
				self.debugLog(u"No bulbId exists in the \"%s\" device. New device perhaps." % (device.name))
				return

		self.debugLog(u"Data from hub: " + r.content)
		# Convert the response to a Python object.
		try:
			bulb = json.loads(r.content)
		except Exception, e:
			indigo.server.log(u"Error retrieving Hue bulb status: " + str(e))
			return False

		### Parse Data
		#
		# Sanity check the returned data first.
		try:
			# If the bulb variable is a list, then there were processing errors.
			errorDict = bulb[0]
			errorText = u"Error retrieving Hue device status: %s" % errorDict['error']['description']
			self.errorLog(errorText)
			return
		except KeyError:
			errorDict = []
			# If there was a KeyError, then there were no processing errors.
		#
		# Data common to all device types...
		#   Value assignments.
		brightness = bulb['state'].get('bri', 0)
		onState = bulb['state'].get('on', False)
		alert = bulb['state'].get('alert', "")
		online = bulb['state'].get('reachable', False)
		nameOnHub = bulb.get('name', "no name")
		modelId = bulb.get('modelid', "")

		#   Value manipulation.
		# Convert brightness from 0-255 range to 0-100 range.
		brightnessLevel = int(round(brightness / 255.0 * 100.0))
		# Compensate for incorrect rounding to zero if original brightness is not zero.
		if brightnessLevel == 0 and brightness > 0:
			brightnessLevel = 1
		# If the "on" state is False, it doesn't matter what brightness the hub
		#   is reporting, the effective brightness is zero.
		if onState == False:
			brightnessLevel = 0

		#   Update Indigo states and properties common to all Hue devices.
		tempProps = device.pluginProps
		# Update the Hue device name.
		if nameOnHub != device.pluginProps.get('nameOnHub', False):
			tempProps['nameOnHub'] = nameOnHub
		# Update the modelId.
		if modelId != device.pluginProps.get('modelId', ""):
			tempProps['modelId'] = modelId
		# If there were property changes, update the device.
		if tempProps != device.pluginProps:
			self.updateDeviceProps(device, tempProps)
		# Update the online status of the Hue device.
		self.updateDeviceState(device, 'online', online)
		# Update the error state if needed.
		if not online:
			device.setErrorStateOnServer("disconnected")
		else:
			device.setErrorStateOnServer("")
		# Update the alert state of the Hue device.
		self.updateDeviceState(device, 'alertMode', alert)

		# Device-type-specific data...

		# -- Hue Bulbs --
		if modelId in kHueBulbDeviceIDs:
			#   Value assignment.  (Using the get() method to avoid KeyErrors).
			hue = bulb['state'].get('hue', 0)
			saturation = bulb['state'].get('sat', 0)
			colorX = bulb['state'].get('xy', [0,0])[0]
			colorY = bulb['state'].get('xy', [0,0])[1]
			colorRed = 255		# Initialize for later
			colorGreen = 255	# Initialize for later
			colorBlue = 255		# Initialize for later
			colorTemp = bulb['state'].get('ct', 0)
			colorMode = bulb['state'].get('colormode', "ct")
			effect = bulb['state'].get('effect', "none")

			#   Value manipulation.
			# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
			hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
			rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
			# RGB values will have a range of 0 to 255.
			colorRed = int(round(rgb.rgb_r))
			colorGreen = int(round(rgb.rgb_g))
			colorBlue = int(round(rgb.rgb_b))
			# Convert saturation from 0-255 scale to 0-100 scale.
			saturation = int(round(saturation / 255.0 * 100.0))
			# Convert hue from 0-65535 scale to 0-360 scale.
			hue = int(round(hue / 182.0))
			# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
			if colorTemp > 0:
				# Converting from mireds to Kelvin.
				colorTemp = int(round(1000000.0/colorTemp))
			else:
				colorTemp = 0

			# Update the Indigo device if the Hue device is on.
			if onState == True:
				tempProps = device.pluginProps
				# Update the brightness level if it's different.
				if device.states['brightnessLevel'] != brightnessLevel:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
				# Hue Degrees (0-360).
				self.updateDeviceState(device, 'hue', hue)
				# Saturation (0-100).
				self.updateDeviceState(device, 'saturation', saturation)
				# CIE XY Cromaticity (range of 0.0 to 1.0 for X and Y)
				self.updateDeviceState(device, 'colorX', colorX)
				self.updateDeviceState(device, 'colorY', colorY)
				# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
				self.updateDeviceState(device, 'colorTemp', colorTemp)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)
				# Red, Green, Blue (0-255).
				self.updateDeviceState(device, 'colorRed', colorRed)
				self.updateDeviceState(device, 'colorGreen', colorGreen)
				self.updateDeviceState(device, 'colorBlue', colorBlue)

				### Update inherited states for Indigo 7+ devices.
				if "whiteLevel" in device.states or "redLevel" in device.states:
					# White Level (negative saturation, 0-100).
					self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
					# White Temperature (0-100).
					self.updateDeviceState(device, 'whiteTemperature', colorTemp)
					# Red, Green, Blue levels (0-100).
					self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
					self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
					self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

			elif onState == False:
				# Hue device is off. Set brightness to zero.
				if device.states['brightnessLevel'] != 0:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', 0)
				# Hue Degrees (convert from 0-65535 to 0-360).
				self.updateDeviceState(device, 'hue', hue)
				# Saturation (convert from 0-255 to 0-100).
				self.updateDeviceState(device, 'saturation', saturation)
				# CIE XY Cromaticity.
				self.updateDeviceState(device, 'colorX', colorX)
				self.updateDeviceState(device, 'colorY', colorY)
				# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
				self.updateDeviceState(device, 'colorTemp', colorTemp)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)
				# Red, Green, and Blue Color.
				#    If the bulb is off, all RGB values should be 0.
				self.updateDeviceState(device, 'colorRed', 0)
				self.updateDeviceState(device, 'colorGreen', 0)
				self.updateDeviceState(device, 'colorBlue', 0)

				### Update inherited states for Indigo 7+ devices.
				if "whiteLevel" in device.states or "redLevel" in device.states:
					# White Level (negative saturation, 0-100).
					self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
					# White Temperature (0-100).
					self.updateDeviceState(device, 'whiteTemperature', colorTemp)
					# Red, Green, Blue levels (0-100).
					self.updateDeviceState(device, 'redLevel', 0)
					self.updateDeviceState(device, 'greenLevel', 0)
					self.updateDeviceState(device, 'blueLevel', 0)
			else:
				# Unrecognized on state, but not important enough to mention in regular log.
				self.debugLog(u"Hue bulb unrecognized on state given by hub: " + str(bulb['state']['on']))

			# Update the effect state (regardless of onState).
			self.updateDeviceState(device, 'effect', effect)

			# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
			for controlDeviceId in self.controlDeviceList:
				controlDevice = indigo.devices[int(controlDeviceId)]
				attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
				if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
					# Device has attributes controlled by a Hue Device Attribute Controler.
					#   Update the controller device based on current bulb device states.
					#   But if the control destination device is off, update the value of the
					#   controller (virtual dimmer) to 0.
					if device.onState == True:
						# Destination Hue Bulb device is on, update Attribute Controller brightness.
						if attributeToControl == "hue":
							# Convert hue scale from 0-360 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
						elif attributeToControl == "saturation":
							self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
						elif attributeToControl == "colorRed":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
						elif attributeToControl == "colorGreen":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
						elif attributeToControl == "colorBlue":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
						elif attributeToControl == "colorTemp":
							# Convert color temperature scale from 2000-6500 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
					else:
						# Hue Device is off.  Set Attribute Controller device brightness level to 0.
						self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

		# -- Ambiance --
		elif modelId in kAmbianceDeviceIDs:
			#   Value assignment.  (Using the get() method to avoid KeyErrors).
			colorTemp = bulb['state'].get('ct', 0)
			colorMode = bulb['state'].get('colormode', "ct")
			effect = bulb['state'].get('effect', "none")

			#   Value manipulation.
			# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
			if colorTemp > 0:
				# Converting from mireds to Kelvin.
				colorTemp = int(round(1000000.0/colorTemp))
			else:
				colorTemp = 0

			# Update the Indigo device if the Hue device is on.
			if onState == True:
				# Update the brightness level if it's different.
				if device.states['brightnessLevel'] != brightnessLevel:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
				# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
				self.updateDeviceState(device, 'colorTemp', colorTemp)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)

				### Update inherited states for Indigo 7+ devices.
				if "whiteLevel" in device.states:
					# White Level (negative saturation, 0-100).
					self.updateDeviceState(device, 'whiteLevel', 100)
					# White Temperature (0-100).
					self.updateDeviceState(device, 'whiteTemperature', colorTemp)

			elif onState == False:
				# Hue device is off. Set brightness to zero.
				if device.states['brightnessLevel'] != 0:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', 0)
				# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
				self.updateDeviceState(device, 'colorTemp', colorTemp)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)

				### Update inherited states for Indigo 7+ devices.
				if "whiteLevel" in device.states:
					# White Level (negative saturation, 0-100).
					self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
					# White Temperature (0-100).
					self.updateDeviceState(device, 'whiteTemperature', colorTemp)
			else:
				# Unrecognized on state, but not important enough to mention in regular log.
				self.debugLog(u"Ambiance light unrecognized \"on\" state given by hub: " + str(bulb['state']['on']))

			# Update the effect state (regardless of onState).
			self.updateDeviceState(device, 'effect', effect)

			# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
			for controlDeviceId in self.controlDeviceList:
				controlDevice = indigo.devices[int(controlDeviceId)]
				attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
				if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
					# Device has attributes controlled by a Hue Device Attribute Controler.
					#   Update the controller device based on current bulb device states.
					#   But if the control destination device is off, update the value of the
					#   controller (virtual dimmer) to 0.
					if device.onState == True:
						# Destination Ambiance light device is on, update Attribute Controller brightness.
						if attributeToControl == "colorTemp":
							# Convert color temperature scale from 2000-6500 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
					else:
						# Hue Device is off.  Set Attribute Controller device brightness level to 0.
						self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

		# -- LightStrips --
		elif modelId in kLightStripsDeviceIDs:
			#   Value assignment.  (Using the get() method to avoid KeyErrors).
			hue = bulb['state'].get('hue', 0)
			saturation = bulb['state'].get('sat', 0)
			colorX = bulb['state'].get('xy', [0,0])[0]
			colorY = bulb['state'].get('xy', [0,0])[1]
			colorRed = 255		# Initialize for later
			colorGreen = 255	# Initialize for later
			colorBlue = 255		# Initialize for later
			# Handle LightStrip Plus color temperature values.
			if bulb['modelid'] == "LST002":
				colorTemp = bulb['state'].get('ct', 0)
			colorMode = bulb['state'].get('colormode', "ct")
			effect = bulb['state'].get('effect', "none")

			#   Value manipulation.
			# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
			hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
			rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
			# RGB values will have a range of 0 to 255.
			colorRed = int(round(rgb.rgb_r))
			colorGreen = int(round(rgb.rgb_g))
			colorBlue = int(round(rgb.rgb_b))
			# Convert saturation from 0-255 scale to 0-100 scale.
			saturation = int(round(saturation / 255.0 * 100.0))
			# Convert hue from 0-65535 scale to 0-360 scale.
			hue = int(round(hue / 182.0))
			# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
			if bulb['modelid'] == "LST002":
				if colorTemp > 0:
					# Converting from mireds to Kelvin.
					colorTemp = int(round(1000000.0/colorTemp))
				else:
					colorTemp = 0

			# Update the Indigo device if the Hue device is on.
			if onState == True:
				tempProps = device.pluginProps
				# Update the brightness level if it's different.
				if device.states['brightnessLevel'] != brightnessLevel:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
				# Hue Degrees (0-360).
				self.updateDeviceState(device, 'hue', hue)
				# Saturation (0-100).
				self.updateDeviceState(device, 'saturation', saturation)
				# CIE XY Cromaticity (range of 0.0 to 1.0 for X and Y)
				self.updateDeviceState(device, 'colorX', colorX)
				self.updateDeviceState(device, 'colorY', colorY)
				# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
				if bulb['modelid'] == "LST002":
					self.updateDeviceState(device, 'colorTemp', colorTemp)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)
				# Red, Green, Blue (0-255).
				self.updateDeviceState(device, 'colorRed', colorRed)
				self.updateDeviceState(device, 'colorGreen', colorGreen)
				self.updateDeviceState(device, 'colorBlue', colorBlue)

				### Update inherited states for Indigo 7+ devices.
				if "whiteLevel" in device.states or "redLevel" in device.states:
					# For LightStrip Plus only...
					if bulb['modelid'] == "LST002":
						# White Level (negative saturation, 0-100).
						self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
						# White Temperature (0-100).
						self.updateDeviceState(device, 'whiteTemperature', colorTemp)
					# Red, Green, Blue levels (0-100).
					self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
					self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
					self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

			elif onState == False:
				# Hue device is off. Set brightness to zero.
				if device.states['brightnessLevel'] != 0:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', 0)
				# Hue Degrees (convert from 0-65535 to 0-360).
				self.updateDeviceState(device, 'hue', hue)
				# Saturation (convert from 0-255 to 0-100).
				self.updateDeviceState(device, 'saturation', saturation)
				# CIE XY Cromaticity.
				self.updateDeviceState(device, 'colorX', colorX)
				self.updateDeviceState(device, 'colorY', colorY)
				# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
				if bulb['modelid'] == "LST002":
					self.updateDeviceState(device, 'colorTemp', colorTemp)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)
				# Red, Green, and Blue Color.
				#    If the bulb is off, all RGB values should be 0.
				self.updateDeviceState(device, 'colorRed', 0)
				self.updateDeviceState(device, 'colorGreen', 0)
				self.updateDeviceState(device, 'colorBlue', 0)

				### Update inherited states for Indigo 7+ devices.
				if "whiteLevel" in device.states or "redLevel" in device.states:
					# For LightStrip Plus only...
					if bulb['modelid'] == "LST002":
						# White Level (negative saturation, 0-100).
						self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
						# White Temperature (0-100).
						self.updateDeviceState(device, 'whiteTemperature', colorTemp)
					# Red, Green, Blue levels (0-100).
					self.updateDeviceState(device, 'redLevel', 0)
					self.updateDeviceState(device, 'greenLevel', 0)
					self.updateDeviceState(device, 'blueLevel', 0)
			else:
				# Unrecognized on state, but not important enough to mention in regular log.
				self.debugLog(u"LightStrip unrecognized on state given by hub: " + str(bulb['state']['on']))

			# Update the effect state (regardless of onState).
			self.updateDeviceState(device, 'effect', effect)

			# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
			for controlDeviceId in self.controlDeviceList:
				controlDevice = indigo.devices[int(controlDeviceId)]
				attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
				if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
					# Device has attributes controlled by a Hue Device Attribute Controler.
					#   Update the controller device based on current bulb device states.
					#   But if the control destination device is off, update the value of the
					#   controller (virtual dimmer) to 0.
					if device.onState == True:
						# Destination Hue Bulb device is on, update Attribute Controller brightness.
						if attributeToControl == "hue":
							# Convert hue scale from 0-360 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
						elif attributeToControl == "saturation":
							self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
						elif attributeToControl == "colorRed":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
						elif attributeToControl == "colorGreen":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
						elif attributeToControl == "colorBlue":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
						elif attributeToControl == "colorTemp" and bulb['modelid'] == "LST002":
							# Convert color temperature scale from 2000-6500 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
					else:
						# Hue Device is off.  Set Attribute Controller device brightness level to 0.
						self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

		# -- LivingColors --
		elif modelId in kLivingColorsDeviceIDs:
			#   Value assignment.
			saturation = bulb['state'].get('sat', "0")
			hue = bulb['state'].get('hue', "0")
			colorX = bulb['state'].get('xy', [0,0])[0]
			colorY = bulb['state'].get('xy', [0,0])[1]
			colorRed = 255		# Initialize for later
			colorGreen = 255	# Initialize for later
			colorBlue = 255		# Initialize for later
			colorMode = bulb['state'].get('colormode', "xy")
			effect = bulb['state'].get('effect', "none")

			#   Value manipulation.
			# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
			hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
			rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
			colorRed = int(round(rgb.rgb_r))
			colorGreen = int(round(rgb.rgb_g))
			colorBlue = int(round(rgb.rgb_b))
			# Convert saturation from 0-255 scale to 0-100 scale.
			saturation = int(round(saturation / 255.0 * 100.0))
			# Convert hue from 0-65535 scale to 0-360 scale.
			hue = int(round(hue / 182.0))

			# Update the Indigo device if the Hue device is on.
			if onState == True:
				# Update the brightness level if it's different.
				if device.states['brightnessLevel'] != brightnessLevel:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
				# Hue Degrees (0-360).
				self.updateDeviceState(device, 'hue', hue)
				#   Saturation (0-100).
				self.updateDeviceState(device, 'saturation', saturation)
				#   CIE XY Cromaticity.
				self.updateDeviceState(device, 'colorX', colorX)
				self.updateDeviceState(device, 'colorY', colorY)
				#   Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)
				#   Red, Green, Blue.
				self.updateDeviceState(device, 'colorRed', colorRed)
				self.updateDeviceState(device, 'colorGreen', colorGreen)
				self.updateDeviceState(device, 'colorBlue', colorBlue)

				### Update inherited states for Indigo 7+ devices.
				if "redLevel" in device.states:
					# Red, Green, Blue levels (0-100).
					self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
					self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
					self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

			elif onState == False:
				# Hue device is off. Set brightness to zero.
				if device.states['brightnessLevel'] != 0:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', 0)
				# Hue Degrees (convert from 0-65535 to 0-360).
				self.updateDeviceState(device, 'hue', hue)
				# Saturation (convert from 0-255 to 0-100).
				self.updateDeviceState(device, 'saturation', saturation)
				# CIE XY Cromaticity.
				self.updateDeviceState(device, 'colorX', colorX)
				self.updateDeviceState(device, 'colorY', colorY)
				# Color Mode.
				self.updateDeviceState(device, 'colorMode', colorMode)
				# Red, Green, and Blue Color.
				#    If the bulb is off, all RGB values should be 0.
				self.updateDeviceState(device, 'colorRed', 0)
				self.updateDeviceState(device, 'colorGreen', 0)
				self.updateDeviceState(device, 'colorBlue', 0)

				### Update inherited states for Indigo 7+ devices.
				if "redLevel" in device.states:
					# Red, Green, Blue levels (0-100).
					self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
					self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
					self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))
			else:
				# Unrecognized on state, but not important enough to mention in regular log.
				self.debugLog(u"LivingColors unrecognized on state given by hub: " + str(bulb['state']['on']))

			# Update the effect state (regardless of onState).
			self.updateDeviceState(device, 'effect', effect)

			# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
			for controlDeviceId in self.controlDeviceList:
				controlDevice = indigo.devices[int(controlDeviceId)]
				attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
				if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
					# Device has attributes controlled by a Hue Device Attribute Controler.
					#   Update the controller device based on current bulb device states.
					#   But if the control destination device is off, update the value of the
					#   controller (virtual dimmer) to 0.
					if device.onState == True:
						# Destination Hue Bulb device is on, update Attribute Controller brightness.
						if attributeToControl == "hue":
							# Convert hue scale from 0-360 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
						elif attributeToControl == "saturation":
							self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
						elif attributeToControl == "colorRed":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
						elif attributeToControl == "colorGreen":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
						elif attributeToControl == "colorBlue":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
					else:
						# Hue Device is off.  Set Attribute Controller device brightness level to 0.
						self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

		# -- LivingWhites --
		elif modelId in kLivingWhitesDeviceIDs:
			# Update the Indigo device if the Hue device is on.
			if onState == True:
				# Update the brightness level if it's different.
				if device.states['brightnessLevel'] != brightnessLevel:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
			elif onState == False:
				# Hue device is off. Set brightness to zero.
				if device.states['brightnessLevel'] != 0:
					# Log the update.
					indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
					self.updateDeviceState(device, 'brightnessLevel', 0)
			else:
				# Unrecognized on state, but not important enough to mention in regular log.
				self.debugLog(u"LivingWhites unrecognized on state given by hub: " + str(bulb['state']['on']))

			# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
			for controlDeviceId in self.controlDeviceList:
				controlDevice = indigo.devices[int(controlDeviceId)]
				attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
				if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
					# Device has attributes controlled by a Hue Device Attribute Controler.
					#   Update the controller device based on current bulb device states.
					#   But if the control destination device is off, update the value of the
					#   controller (virtual dimmer) to 0.
					if device.onState == True:
						# Destination Hue Bulb device is on, update Attribute Controller brightness.
						if attributeToControl == "hue":
							# Convert hue scale from 0-360 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
						elif attributeToControl == "saturation":
							self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
						elif attributeToControl == "colorRed":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
						elif attributeToControl == "colorGreen":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
						elif attributeToControl == "colorBlue":
							# Convert RGB scale from 0-255 to 0-100.
							self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
					else:
						# Hue Device is off.  Set Attribute Controller device brightness level to 0.
						self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

		else:
			# Unrecognized model ID.
			if not self.unsupportedDeviceWarned:
				errorText = u"The \"" + device.name + u"\" device has an unrecognized model ID of \"" + bulb.get('modelid', "") + u"\". Hue Lights plugin does not support this device."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				self.unsupportedDeviceWarned = True

	# Parse Hue Lights Data
	########################################
	def parseHueLightsData(self, hubDevice):
		self.debugLog(u"Starting parseHueLightsData.")

		# Iterate through all the Indigo devices and look for Hue light changes in the
		#   self.lightsDict that changed, then update the Indigo device states and properties
		#   as needed.  This method does no actual Hue hub communication.  It just updates
		#   Indigo devices with information already obtained through the use of the
		#   self.updateLightsList.

		self.debugLog(u"parseHueLightsData: There are %i lights on the Hue bridge and %i Indigo devices controlling Hue lights and groups." % (len(self.lightsDict), len(self.deviceList)))
		# Start going through all the devices in the self.deviceList and update any Indigo
		#   devices that are controlling the Hue light devices.
		for deviceId in self.deviceList:
			device = indigo.devices[deviceId]
			self.debugLog(u"parseHueLightsData: Looking at Indigo device \"%s\"." % (device.name))

			# Get the hub ID
			hubId = device.pluginProps.get("hubId", "INVALID")

			# If this Indigo device is not for a Hue Group or a Hue Hub...
			if device.deviceTypeId != "hueGroup" and device.deviceTypeId != "hueHub":
				self.debugLog(u"parseHueLightsData: Indigo device \"%s\" is not for a Hue group. Proceeding." % (device.name))
				# Go through each Hue light device and see if it is controlled by this Indigo device.
				for bulbId in self.lightsDict[hubId]:

					bulb = self.lightsDict[hubId][bulbId]
					self.debugLog(u"parseHueLightsData: Parsing Hue device ID %s (\"%s\")." % (bulbId, bulb.get('name', "no name")))

					# Separate out the specific Hue bulb data.
					# Is this Hue device ID the one associated with this Indigo device?
					if bulbId == device.pluginProps['bulbId']:
						self.debugLog(u"parseHueLightsData: Indigo device \"%s\" is controlling Hue device ID \"%s\" (\"%s\"). Updating Indigo device properties and states." % (device.name, bulbId, bulb.get('name', "no name")))
						# Data common to all device types...
						#   Value assignments.
						brightness = bulb['state'].get('bri', 0)
						onState = bulb['state'].get('on', False)
						alert = bulb['state'].get('alert', "")
						online = bulb['state'].get('reachable', False)
						nameOnHub = bulb.get('name', "no name")
						modelId = bulb.get('modelid', "")
						manufacturerName = bulb.get('manufacturername', "")
						swVersion = bulb.get('swversion', "")
						type = bulb.get('type', "")
						uniqueId = bulb.get('uniqueid', "")

						#   Value manipulation.
						# Convert brightness from 0-255 range to 0-100 range.
						brightnessLevel = int(round(brightness / 255.0 * 100.0))
						# Compensate for incorrect rounding to zero if original brightness is not zero.
						if brightnessLevel == 0 and brightness > 0:
							brightnessLevel = 1
						# If the "on" state is False, it doesn't matter what brightness the hub
						#   is reporting, the effective brightness is zero.
						if onState == False:
							brightnessLevel = 0

						#   Update Indigo states and properties common to all Hue devices.
						tempProps = device.pluginProps
						# Update the Hue device name.
						if nameOnHub != device.pluginProps.get('nameOnHub', False):
							tempProps['nameOnHub'] = nameOnHub
						# Update the modelId.
						if modelId != device.pluginProps.get('modelId', ""):
							tempProps['modelId'] = modelId
						# Update the manufacturer name.
						if manufacturerName != device.pluginProps.get('manufacturerName', ""):
							tempProps['manufacturerName'] = manufacturerName
						# Update the software version for the device on the Hue hub.
						if swVersion != device.pluginProps.get('swVersion', ""):
							tempProps['swVersion'] = swVersion
						# Update the type as defined by Hue.
						if type != device.pluginProps.get('type', ""):
							tempProps['type'] = type
						# Update the unique ID (MAC address) of the Hue device.
						if uniqueId != device.pluginProps.get('uniqueId', ""):
							tempProps['uniqueId'] = uniqueId
						# If there were property changes, update the device.
						if tempProps != device.pluginProps:
							self.updateDeviceProps(device, tempProps)
						# Update the online status of the Hue device.
						self.updateDeviceState(device, 'online', online)
						# Update the error state if needed.
						if not online:
							device.setErrorStateOnServer("disconnected")
						else:
							device.setErrorStateOnServer("")
						# Update the alert state of the Hue device.
						self.updateDeviceState(device, 'alertMode', alert)

						# Device-type-specific data...

						# -- Hue Bulbs --
						if modelId in kHueBulbDeviceIDs:
							#   Value assignment.  (Using the get() method to avoid KeyErrors).
							hue = bulb['state'].get('hue', 0)
							saturation = bulb['state'].get('sat', 0)
							colorX = bulb['state'].get('xy', [0,0])[0]
							colorY = bulb['state'].get('xy', [0,0])[1]
							colorRed = 255		# Initialize for later
							colorGreen = 255	# Initialize for later
							colorBlue = 255		# Initialize for later
							colorTemp = bulb['state'].get('ct', 0)
							colorMode = bulb['state'].get('colormode', "ct")
							effect = bulb['state'].get('effect', "none")

							#   Value manipulation.
							# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
							hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
							rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
							# RGB values will have a range of 0 to 255.
							colorRed = int(round(rgb.rgb_r))
							colorGreen = int(round(rgb.rgb_g))
							colorBlue = int(round(rgb.rgb_b))
							# Convert saturation from 0-255 scale to 0-100 scale.
							saturation = int(round(saturation / 255.0 * 100.0))
							# Convert hue from 0-65535 scale to 0-360 scale.
							hue = int(round(hue / 182.0))
							# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
							if colorTemp > 0:
								# Converting from mireds to Kelvin.
								colorTemp = int(round(1000000.0/colorTemp))
							else:
								colorTemp = 0

							# Update the Indigo device if the Hue device is on.
							if onState == True:
								tempProps = device.pluginProps
								# Update the brightness level if it's different.
								if device.states['brightnessLevel'] != brightnessLevel:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
								# Hue Degrees (0-360).
								self.updateDeviceState(device, 'hue', hue)
								# Saturation (0-100).
								self.updateDeviceState(device, 'saturation', saturation)
								# CIE XY Cromaticity (range of 0.0 to 1.0 for X and Y)
								self.updateDeviceState(device, 'colorX', colorX)
								self.updateDeviceState(device, 'colorY', colorY)
								# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
								self.updateDeviceState(device, 'colorTemp', colorTemp)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)
								# Red, Green, Blue (0-255).
								self.updateDeviceState(device, 'colorRed', colorRed)
								self.updateDeviceState(device, 'colorGreen', colorGreen)
								self.updateDeviceState(device, 'colorBlue', colorBlue)

								### Update inherited states for Indigo 7+ devices.
								if "whiteLevel" in device.states or "redLevel" in device.states:
									# White Level (negative saturation, 0-100).
									self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
									# White Temperature (0-100).
									self.updateDeviceState(device, 'whiteTemperature', colorTemp)
									# Red, Green, Blue levels (0-100).
									self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
									self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
									self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

							elif onState == False:
								# Hue device is off. Set brightness to zero.
								if device.states['brightnessLevel'] != 0:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', 0)
								# Hue Degrees (convert from 0-65535 to 0-360).
								self.updateDeviceState(device, 'hue', hue)
								# Saturation (convert from 0-255 to 0-100).
								self.updateDeviceState(device, 'saturation', saturation)
								# CIE XY Cromaticity.
								self.updateDeviceState(device, 'colorX', colorX)
								self.updateDeviceState(device, 'colorY', colorY)
								# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
								self.updateDeviceState(device, 'colorTemp', colorTemp)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)
								# Red, Green, and Blue Color.
								#    If the bulb is off, all RGB values should be 0.
								self.updateDeviceState(device, 'colorRed', 0)
								self.updateDeviceState(device, 'colorGreen', 0)
								self.updateDeviceState(device, 'colorBlue', 0)

								### Update inherited states for Indigo 7+ devices.
								if "whiteLevel" in device.states or "redLevel" in device.states:
									# White Level (negative saturation, 0-100).
									self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
									# White Temperature (0-100).
									self.updateDeviceState(device, 'whiteTemperature', colorTemp)
									# Red, Green, Blue levels (0-100).
									self.updateDeviceState(device, 'redLevel', 0)
									self.updateDeviceState(device, 'greenLevel', 0)
									self.updateDeviceState(device, 'blueLevel', 0)
							else:
								# Unrecognized on state, but not important enough to mention in regular log.
								self.debugLog(u"Hue bulb unrecognized on state given by hub: " + str(bulb['state']['on']))

							# Update the effect state (regardless of onState).
							self.updateDeviceState(device, 'effect', effect)

							# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
							for controlDeviceId in self.controlDeviceList:
								controlDevice = indigo.devices[int(controlDeviceId)]
								attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
								if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
									# Device has attributes controlled by a Hue Device Attribute Controler.
									#   Update the controller device based on current bulb device states.
									#   But if the control destination device is off, update the value of the
									#   controller (virtual dimmer) to 0.
									if device.onState == True:
										# Destination Hue Bulb device is on, update Attribute Controller brightness.
										if attributeToControl == "hue":
											# Convert hue scale from 0-360 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
										elif attributeToControl == "saturation":
											self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
										elif attributeToControl == "colorRed":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
										elif attributeToControl == "colorGreen":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
										elif attributeToControl == "colorBlue":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
										elif attributeToControl == "colorTemp":
											# Convert color temperature scale from 2000-6500 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
									else:
										# Hue Device is off.  Set Attribute Controller device brightness level to 0.
										self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

						# -- Ambiance --
						elif modelId in kAmbianceDeviceIDs:
							#   Value assignment.  (Using the get() method to avoid KeyErrors).
							colorTemp = bulb['state'].get('ct', 0)
							colorMode = bulb['state'].get('colormode', "ct")
							effect = bulb['state'].get('effect', "none")

							#   Value manipulation.
							# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
							if colorTemp > 0:
								# Converting from mireds to Kelvin.
								colorTemp = int(round(1000000.0/colorTemp))
							else:
								colorTemp = 0

							# Update the Indigo device if the Hue device is on.
							if onState == True:
								# Update the brightness level if it's different.
								if device.states['brightnessLevel'] != brightnessLevel:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
								# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
								self.updateDeviceState(device, 'colorTemp', colorTemp)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)

								### Update inherited states for Indigo 7+ devices.
								if "whiteLevel" in device.states:
									# White Level (negative saturation, 0-100).
									self.updateDeviceState(device, 'whiteLevel', 100)
									# White Temperature (0-100).
									self.updateDeviceState(device, 'whiteTemperature', colorTemp)

							elif onState == False:
								# Hue device is off. Set brightness to zero.
								if device.states['brightnessLevel'] != 0:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', 0)
								# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
								self.updateDeviceState(device, 'colorTemp', colorTemp)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)

								### Update inherited states for Indigo 7+ devices.
								if "whiteLevel" in device.states:
									# White Level (negative saturation, 0-100).
									self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
									# White Temperature (0-100).
									self.updateDeviceState(device, 'whiteTemperature', colorTemp)
							else:
								# Unrecognized on state, but not important enough to mention in regular log.
								self.debugLog(u"Ambiance light unrecognized \"on\" state given by hub: " + str(bulb['state']['on']))

							# Update the effect state (regardless of onState).
							self.updateDeviceState(device, 'effect', effect)

							# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
							for controlDeviceId in self.controlDeviceList:
								controlDevice = indigo.devices[int(controlDeviceId)]
								attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
								if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
									# Device has attributes controlled by a Hue Device Attribute Controler.
									#   Update the controller device based on current bulb device states.
									#   But if the control destination device is off, update the value of the
									#   controller (virtual dimmer) to 0.
									if device.onState == True:
										# Destination Ambiance light device is on, update Attribute Controller brightness.
										if attributeToControl == "colorTemp":
											# Convert color temperature scale from 2000-6500 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
									else:
										# Hue Device is off.  Set Attribute Controller device brightness level to 0.
										self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

						# -- LightStrips --
						elif modelId in kLightStripsDeviceIDs:
							#   Value assignment.  (Using the get() method to avoid KeyErrors).
							hue = bulb['state'].get('hue', 0)
							saturation = bulb['state'].get('sat', 0)
							colorX = bulb['state'].get('xy', [0,0])[0]
							colorY = bulb['state'].get('xy', [0,0])[1]
							colorRed = 255		# Initialize for later
							colorGreen = 255	# Initialize for later
							colorBlue = 255		# Initialize for later
							# Handle LightStrip Plus color temperature values.
							if bulb['modelid'] == "LST002":
								colorTemp = bulb['state'].get('ct', 0)
							colorMode = bulb['state'].get('colormode', "ct")
							effect = bulb['state'].get('effect', "none")

							#   Value manipulation.
							# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
							hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
							rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
							# RGB values will have a range of 0 to 255.
							colorRed = int(round(rgb.rgb_r))
							colorGreen = int(round(rgb.rgb_g))
							colorBlue = int(round(rgb.rgb_b))
							# Convert saturation from 0-255 scale to 0-100 scale.
							saturation = int(round(saturation / 255.0 * 100.0))
							# Convert hue from 0-65535 scale to 0-360 scale.
							hue = int(round(hue / 182.0))
							# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
							if bulb['modelid'] == "LST002":
								if colorTemp > 0:
									# Converting from mireds to Kelvin.
									colorTemp = int(round(1000000.0/colorTemp))
								else:
									colorTemp = 0

							# Update the Indigo device if the Hue device is on.
							if onState == True:
								tempProps = device.pluginProps
								# Update the brightness level if it's different.
								if device.states['brightnessLevel'] != brightnessLevel:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
								# Hue Degrees (0-360).
								self.updateDeviceState(device, 'hue', hue)
								# Saturation (0-100).
								self.updateDeviceState(device, 'saturation', saturation)
								# CIE XY Cromaticity (range of 0.0 to 1.0 for X and Y)
								self.updateDeviceState(device, 'colorX', colorX)
								self.updateDeviceState(device, 'colorY', colorY)
								# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
								if bulb['modelid'] == "LST002":
									self.updateDeviceState(device, 'colorTemp', colorTemp)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)
								# Red, Green, Blue (0-255).
								self.updateDeviceState(device, 'colorRed', colorRed)
								self.updateDeviceState(device, 'colorGreen', colorGreen)
								self.updateDeviceState(device, 'colorBlue', colorBlue)

								### Update inherited states for Indigo 7+ devices.
								if "whiteLevel" in device.states or "redLevel" in device.states:
									# For LightStrip Plus only...
									if bulb['modelid'] == "LST002":
										# White Level (negative saturation, 0-100).
										self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
										# White Temperature (0-100).
										self.updateDeviceState(device, 'whiteTemperature', colorTemp)
									# Red, Green, Blue levels (0-100).
									self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
									self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
									self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

							elif onState == False:
								# Hue device is off. Set brightness to zero.
								if device.states['brightnessLevel'] != 0:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', 0)
								# Hue Degrees (convert from 0-65535 to 0-360).
								self.updateDeviceState(device, 'hue', hue)
								# Saturation (convert from 0-255 to 0-100).
								self.updateDeviceState(device, 'saturation', saturation)
								# CIE XY Cromaticity.
								self.updateDeviceState(device, 'colorX', colorX)
								self.updateDeviceState(device, 'colorY', colorY)
								# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
								if bulb['modelid'] == "LST002":
									self.updateDeviceState(device, 'colorTemp', colorTemp)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)
								# Red, Green, and Blue Color.
								#    If the bulb is off, all RGB values should be 0.
								self.updateDeviceState(device, 'colorRed', 0)
								self.updateDeviceState(device, 'colorGreen', 0)
								self.updateDeviceState(device, 'colorBlue', 0)

								### Update inherited states for Indigo 7+ devices.
								if "whiteLevel" in device.states or "redLevel" in device.states:
									# For LightStrip Plus only...
									if bulb['modelid'] == "LST002":
										# White Level (negative saturation, 0-100).
										self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
										# White Temperature (0-100).
										self.updateDeviceState(device, 'whiteTemperature', colorTemp)
									# Red, Green, Blue levels (0-100).
									self.updateDeviceState(device, 'redLevel', 0)
									self.updateDeviceState(device, 'greenLevel', 0)
									self.updateDeviceState(device, 'blueLevel', 0)
							else:
								# Unrecognized on state, but not important enough to mention in regular log.
								self.debugLog(u"LightStrip unrecognized on state given by hub: " + str(bulb['state']['on']))

							# Update the effect state (regardless of onState).
							self.updateDeviceState(device, 'effect', effect)

							# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
							for controlDeviceId in self.controlDeviceList:
								controlDevice = indigo.devices[int(controlDeviceId)]
								attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
								if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
									# Device has attributes controlled by a Hue Device Attribute Controler.
									#   Update the controller device based on current bulb device states.
									#   But if the control destination device is off, update the value of the
									#   controller (virtual dimmer) to 0.
									if device.onState == True:
										# Destination Hue Bulb device is on, update Attribute Controller brightness.
										if attributeToControl == "hue":
											# Convert hue scale from 0-360 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
										elif attributeToControl == "saturation":
											self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
										elif attributeToControl == "colorRed":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
										elif attributeToControl == "colorGreen":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
										elif attributeToControl == "colorBlue":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
										elif attributeToControl == "colorTemp" and bulb['modelid'] == "LST002":
											# Convert color temperature scale from 2000-6500 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
									else:
										# Hue Device is off.  Set Attribute Controller device brightness level to 0.
										self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

						# -- LivingColors --
						elif modelId in kLivingColorsDeviceIDs:
							#   Value assignment.
							saturation = bulb['state'].get('sat', "0")
							hue = bulb['state'].get('hue', "0")
							colorX = bulb['state'].get('xy', [0,0])[0]
							colorY = bulb['state'].get('xy', [0,0])[1]
							colorRed = 255		# Initialize for later
							colorGreen = 255	# Initialize for later
							colorBlue = 255		# Initialize for later
							colorMode = bulb['state'].get('colormode', "xy")
							effect = bulb['state'].get('effect', "none")

							#   Value manipulation.
							# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
							hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
							rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
							colorRed = int(round(rgb.rgb_r))
							colorGreen = int(round(rgb.rgb_g))
							colorBlue = int(round(rgb.rgb_b))
							# Convert saturation from 0-255 scale to 0-100 scale.
							saturation = int(round(saturation / 255.0 * 100.0))
							# Convert hue from 0-65535 scale to 0-360 scale.
							hue = int(round(hue / 182.0))

							# Update the Indigo device if the Hue device is on.
							if onState == True:
								# Update the brightness level if it's different.
								if device.states['brightnessLevel'] != brightnessLevel:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
								# Hue Degrees (0-360).
								self.updateDeviceState(device, 'hue', hue)
								#   Saturation (0-100).
								self.updateDeviceState(device, 'saturation', saturation)
								#   CIE XY Cromaticity.
								self.updateDeviceState(device, 'colorX', colorX)
								self.updateDeviceState(device, 'colorY', colorY)
								#   Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)
								#   Red, Green, Blue.
								self.updateDeviceState(device, 'colorRed', colorRed)
								self.updateDeviceState(device, 'colorGreen', colorGreen)
								self.updateDeviceState(device, 'colorBlue', colorBlue)

								### Update inherited states for Indigo 7+ devices.
								if "redLevel" in device.states:
									# Red, Green, Blue levels (0-100).
									self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
									self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
									self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

							elif onState == False:
								# Hue device is off. Set brightness to zero.
								if device.states['brightnessLevel'] != 0:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', 0)
								# Hue Degrees (convert from 0-65535 to 0-360).
								self.updateDeviceState(device, 'hue', hue)
								# Saturation (convert from 0-255 to 0-100).
								self.updateDeviceState(device, 'saturation', saturation)
								# CIE XY Cromaticity.
								self.updateDeviceState(device, 'colorX', colorX)
								self.updateDeviceState(device, 'colorY', colorY)
								# Color Mode.
								self.updateDeviceState(device, 'colorMode', colorMode)
								# Red, Green, and Blue Color.
								#    If the bulb is off, all RGB values should be 0.
								self.updateDeviceState(device, 'colorRed', 0)
								self.updateDeviceState(device, 'colorGreen', 0)
								self.updateDeviceState(device, 'colorBlue', 0)

								### Update inherited states for Indigo 7+ devices.
								if "redLevel" in device.states:
									# Red, Green, Blue levels (0-100).
									self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
									self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
									self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))
							else:
								# Unrecognized on state, but not important enough to mention in regular log.
								self.debugLog(u"LivingColors unrecognized on state given by hub: " + str(bulb['state']['on']))

							# Update the effect state (regardless of onState).
							self.updateDeviceState(device, 'effect', effect)

							# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
							for controlDeviceId in self.controlDeviceList:
								controlDevice = indigo.devices[int(controlDeviceId)]
								attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
								if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
									# Device has attributes controlled by a Hue Device Attribute Controler.
									#   Update the controller device based on current bulb device states.
									#   But if the control destination device is off, update the value of the
									#   controller (virtual dimmer) to 0.
									if device.onState == True:
										# Destination Hue Bulb device is on, update Attribute Controller brightness.
										if attributeToControl == "hue":
											# Convert hue scale from 0-360 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
										elif attributeToControl == "saturation":
											self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
										elif attributeToControl == "colorRed":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
										elif attributeToControl == "colorGreen":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
										elif attributeToControl == "colorBlue":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
									else:
										# Hue Device is off.  Set Attribute Controller device brightness level to 0.
										self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

						# -- LivingWhites --
						elif modelId in kLivingWhitesDeviceIDs:
							# Update the Indigo device if the Hue device is on.
							if onState == True:
								# Update the brightness level if it's different.
								if device.states['brightnessLevel'] != brightnessLevel:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
							elif onState == False:
								# Hue device is off. Set brightness to zero.
								if device.states['brightnessLevel'] != 0:
									# Log the update.
									indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
									self.updateDeviceState(device, 'brightnessLevel', 0)
							else:
								# Unrecognized on state, but not important enough to mention in regular log.
								self.debugLog(u"LivingWhites unrecognized on state given by hub: " + str(bulb['state']['on']))

							# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
							for controlDeviceId in self.controlDeviceList:
								controlDevice = indigo.devices[int(controlDeviceId)]
								attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
								if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
									# Device has attributes controlled by a Hue Device Attribute Controler.
									#   Update the controller device based on current bulb device states.
									#   But if the control destination device is off, update the value of the
									#   controller (virtual dimmer) to 0.
									if device.onState == True:
										# Destination Hue Bulb device is on, update Attribute Controller brightness.
										if attributeToControl == "hue":
											# Convert hue scale from 0-360 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
										elif attributeToControl == "saturation":
											self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
										elif attributeToControl == "colorRed":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
										elif attributeToControl == "colorGreen":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
										elif attributeToControl == "colorBlue":
											# Convert RGB scale from 0-255 to 0-100.
											self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
									else:
										# Hue Device is off.  Set Attribute Controller device brightness level to 0.
										self.updateDeviceState(controlDevice, 'brightnessLevel', 0)

						else:
							# Unrecognized model ID.
							if not self.unsupportedDeviceWarned:
								errorText = u"The \"" + device.name + u"\" device has an unrecognized model ID of \"" + bulb.get('modelid', "") + u"\". Hue Lights plugin does not support this device."
								self.errorLog(errorText)
								# Remember the error.
								self.lastErrorMessage = errorText
								self.unsupportedDeviceWarned = True
						# End of model ID matching if/then test.

						# Since only 1 Indigo device can control 1 Hue device, there's no need
						#    to continue the loop, so we're breaking out of the device matching loop.
						break

					# End check if this Hue device ID is for this Indigo device.
				# End loop through self.lightsDict.
			# End check if this is not a Hue Group device.
		# End loop through self.deviceList.

	# Get Group Status
	########################################
	def getGroupStatus(self, deviceId):
		# Get group status.

		device = indigo.devices[deviceId]

		# Get the hub
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for group '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub device with id '%i'" % (hubId))
			return

		# Get the groupId from the device properties.
		groupId = device.pluginProps.get('groupId', -1)
		self.debugLog(u"Get group status for group %s." % (groupId))
		# if the groupId exists, get the group status.
		if groupId > -1:
			command = "http://%s/api/%s/groups/%s" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.get(command, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
		# There's no groupId provided.
		else:
			self.debugLog(u"No group ID was provided.")
			return

		self.debugLog(u"Data from hub: " + r.content)

		# Convert the response to a Python object.
		try:
			group = json.loads(r.content)
		except Exception, e:
			indigo.server.log(u"Error retrieving Hue group status: " + str(e))
			return

		#
		### Parse Data
		#
		# Sanity check the returned data first.
		try:
			# If the bulb variable is a list, then there were processing errors.
			errorDict = group[0]
			errorText = u"Error retrieving Hue device status: %s" % errorDict['error']['description']
			self.errorLog(errorText)
			return
		except KeyError:
			errorDict = []
		# If there was a KeyError, then there were no processing errors.
		#
		# Value assignments.
		modelId = group.get('modelId', "")
		# Get the name of the group as it appears on the Hue hub.
		nameOnHub = group.get('name', "")
		brightness = group['action'].get('bri', "0")
		onState = group['action'].get('on', False)
		effect = group['action'].get('effect', "")
		alert = group['action'].get('alert', "")
		# Use a generic yellow hue as default if there isn't a hue.
		hue = group['action'].get('hue', 10920)
		saturation = group['action'].get('sat', 0)
		# Use a neutral colorX and Y value as default if one isn't there.
		colorX = group['action'].get('xy', [0.5128, 0.4147])[0]
		colorY = group['action'].get('xy', [0.5128, 0.4147])[1]
		colorRed = 255		# Initialize for later
		colorGreen = 255	# Initialize for later
		colorBlue = 255		# Initialize for later
		# Assign a generic 2800 K (357 mired) color temperature if one doesn't exist.
		colorTemp = group['action'].get('ct', 357)
		# Use "ct" as the color mode if one wasn't specified.
		colorMode = group['action'].get('colormode', "ct")
		# groupMemberIDs is populated a few lines down.
		groupMemberIDs = ""

		i = 0		# To count members in group.
		for tempMemberID in group['lights']:
			if i > 0:
				groupMemberIDs = groupMemberIDs + ", " + str(tempMemberID)
			else:
				groupMemberIDs = tempMemberID
			i += 1
		# Clear the "i" variable.
		del i

		#   Value manipulation.
		# Convert brightness from 0-255 range to 0-100 range.
		brightnessLevel = int(round(brightness / 255.0 * 100.0))
		# Compensate for incorrect rounding to zero if original brightness is not zero.
		if brightnessLevel == 0 and brightness > 0:
			brightnessLevel = 1
		# If the "on" state is False, it doesn't matter what brightness the hub
		#   is reporting, the effective brightness is zero.
		if onState == False:
			brightnessLevel = 0
		# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
		hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
		rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
		colorRed = int(round(rgb.rgb_r))
		colorGreen = int(round(rgb.rgb_g))
		colorBlue = int(round(rgb.rgb_b))
		# Convert saturation from 0-255 scale to 0-100 scale.
		saturation = int(round(saturation / 255.0 * 100.0))
		# Convert hue from 0-65535 scale to 0-360 scale.
		hue = int(round(hue / 182.0))
		# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
		if colorTemp > 0:
			# Converting from mireds to Kelvin.
			colorTemp = int(round(1000000.0/colorTemp))
		else:
			colorTemp = 0

		#   Update Indigo states and properties common to all Hue devices.
		tempProps = device.pluginProps
		# Update the Hue device name.
		if nameOnHub != tempProps.get('nameOnHub', False):
			tempProps['nameOnHub'] = nameOnHub
			self.updateDeviceProps(device, tempProps)
		# Update the modelId.
		if modelId != device.pluginProps.get('modelId', ""):
			tempProps['modelId'] = modelId
			self.updateDeviceProps(device, tempProps)
		# Update the alert state of the Hue device.
		self.updateDeviceState(device, 'alertMode', alert)
		# Update the effect state of the Hue device.
		self.updateDeviceState(device, 'effect', effect)
		# Update the group member IDs.
		self.updateDeviceState(device, 'groupMemberIDs', groupMemberIDs)

		# Update the Indigo device if the Hue group is on.
		if onState == True:
			# Update the brightness level if it's different.
			if device.states['brightnessLevel'] != brightnessLevel:
				# Log the update.
				indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
				self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
			# Hue Degrees (0-360).
			self.updateDeviceState(device, 'hue', hue)
			# Saturation (0-100).
			self.updateDeviceState(device, 'saturation', saturation)
			# CIE XY Cromaticity.
			self.updateDeviceState(device, 'colorX', colorX)
			self.updateDeviceState(device, 'colorY', colorY)
			# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
			self.updateDeviceState(device, 'colorTemp', colorTemp)
			# Color Mode.
			self.updateDeviceState(device, 'colorMode', colorMode)
			# Red, Green, Blue.
			self.updateDeviceState(device, 'colorRed', colorRed)
			self.updateDeviceState(device, 'colorGreen', colorGreen)
			self.updateDeviceState(device, 'colorBlue', colorBlue)

			### Update inherited states for Indigo 7+ devices.
			if "whiteLevel" in device.states or "redLevel" in device.states:
				# White Level (negative saturation, 0-100).
				self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
				# White Temperature (0-100).
				self.updateDeviceState(device, 'whiteTemperature', colorTemp)
				# Red, Green, Blue levels (0-100).
				self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
				self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
				self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

		elif onState == False:
			# Hue group is off. Set brightness to zero.
			if device.states['brightnessLevel'] != 0:
				# Log the update.
				indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
				self.updateDeviceState(device, 'brightnessLevel', 0)
			# Hue Degrees (convert from 0-65535 to 0-360).
			self.updateDeviceState(device, 'hue', hue)
			# Saturation (convert from 0-255 to 0-100).
			self.updateDeviceState(device, 'saturation', saturation)
			# CIE XY Cromaticity.
			self.updateDeviceState(device, 'colorX', colorX)
			self.updateDeviceState(device, 'colorY', colorY)
			# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
			self.updateDeviceState(device, 'colorTemp', colorTemp)
			# Color Mode.
			self.updateDeviceState(device, 'colorMode', colorMode)
			# Red, Green, and Blue Color.
			#    If the bulb is off, all RGB values should be 0.
			self.updateDeviceState(device, 'colorRed', 0)
			self.updateDeviceState(device, 'colorGreen', 0)
			self.updateDeviceState(device, 'colorBlue', 0)
			# Effect
			self.updateDeviceState(device, 'effect', "")
			# Alert
			self.updateDeviceState(device, 'alertMode', "")

			### Update inherited states for Indigo 7+ devices.
			if "whiteLevel" in device.states or "redLevel" in device.states:
				# White Level (negative saturation, 0-100).
				self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
				# White Temperature (0-100).
				self.updateDeviceState(device, 'whiteTemperature', colorTemp)
				# Red, Green, Blue levels (0-100).
				self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
				self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
				self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))
		else:
			# Unrecognized on state, but not important enough to mention in regular log.
			self.debugLog(u"Hue group unrecognized on state given by hub: " + str(group['action']['on']))

		# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
		for controlDeviceId in self.controlDeviceList:
			controlDevice = indigo.devices[int(controlDeviceId)]
			attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
			if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
				# Device has attributes controlled by a Hue Device Attribute Controler.
				#   Update the controller device based on current bulb device states.
				#   But if the control destination device is off, update the value of the
				#   controller (virtual dimmer) to 0.
				if device.onState == True:
					# Destination Hue Bulb device is on, update Attribute Controller brightness.
					if attributeToControl == "hue":
						# Convert hue scale from 0-360 to 0-100.
						self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
					elif attributeToControl == "saturation":
						self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
					elif attributeToControl == "colorRed":
						# Convert RGB scale from 0-255 to 0-100.
						self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
					elif attributeToControl == "colorGreen":
						# Convert RGB scale from 0-255 to 0-100.
						self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
					elif attributeToControl == "colorBlue":
						# Convert RGB scale from 0-255 to 0-100.
						self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
					elif attributeToControl == "colorTemp":
						# Convert color temperature scale from 2000-6500 to 0-100.
						self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
				else:
					# Indigo Device is off.  Set Attribute Controller device brightness level to 0.
					self.updateDeviceState(controlDevice, 'brightnessLevel', 0)


	# Parse Hue Groups Data
	########################################
	def parseHueGroupsData(self, hubDevice):
		self.debugLog(u"Starting parseHueGroupsData.")

		# Itterate through all the Indigo devices and look for Hue group changes in the
		#   self.groupsDict that changed, then update the Indigo device states and properties
		#   as needed.  This method does no actual Hue hub communication.  It just updates
		#   Indigo devices with information already obtained through the use of the
		#   self.updateGroupsList.

		hubGroupsDict = self.groupsDict.get(str(hubDevice.id), dict())

		self.debugLog(u"parseHueGroupsData: There are %i groups on the Hue bridge and %i Indigo devices controlling Hue lights and groups." % (len(hubGroupsDict), len(self.deviceList)))
		# Start going through all the devices in the self.deviceList and update any Indigo
		#   devices that are controlling the Hue group devices.
		for deviceId in self.deviceList:

			device = indigo.devices[deviceId]
			hubId = device.pluginProps.get("hubId", "INVALID")

			self.debugLog(u"parseHueGroupsData: Looking at Indigo device \"%s\"." % (device.name))

			# If this Indigo device is for a Hue Group...
			if device.deviceTypeId == "hueGroup":
				self.debugLog(u"parseHueGroupsData: Indigo device \"%s\" is for a Hue group. Proceeing." % (device.name))
				# Go through each Hue group device and see if it is controlled by this Indigo device.
				for groupId in self.groupsDict[hubdId]:
					group = self.groupsDict[hubId][groupId]
					self.debugLog(u"parseHueGroupsData: Parsing Hue group ID %s (\"%s\")." % (groupId, group.get('name', "no name")))

					# Separate out the specific Hue group data.
					# Is this Hue group ID the one associated with this Indigo device?
					if groupId == device.pluginProps['groupId']:
						self.debugLog(u"parseHueGroupsData: Indigo device \"%s\" is controlling Hue group ID \"%s\" (\"%s\"). Updating Indigo device properties and states." % (device.name, groupId, group.get('name', "no name")))
						# Value assignments.
						# Get the name of the group as it appears on the Hue hub.
						nameOnHub = group.get('name', "")
						groupType = group.get('type', "")
						groupClass = group.get('class', "")
						brightness = group['action'].get('bri', "0")
						onState = group['action'].get('on', False)
						allOn = group['state'].get('all_on', False)
						anyOn = group['state'].get('any_on', False)
						effect = group['action'].get('effect', "")
						alert = group['action'].get('alert', "")
						# Use a generic yellow hue as default if there isn't a hue.
						hue = group['action'].get('hue', 10920)
						saturation = group['action'].get('sat', 0)
						# Use a neutral colorX and Y value as default if one isn't there.
						colorX = group['action'].get('xy', [0.5128, 0.4147])[0]
						colorY = group['action'].get('xy', [0.5128, 0.4147])[1]
						colorRed = 255		# Initialize for later
						colorGreen = 255	# Initialize for later
						colorBlue = 255		# Initialize for later
						# Assign a generic 2800 K (357 mired) color temperature if one doesn't exist.
						colorTemp = group['action'].get('ct', 357)
						# Use "ct" as the color mode if one wasn't specified.
						colorMode = group['action'].get('colormode', "ct")
						# groupMemberIDs is populated a few lines down.
						groupMemberIDs = ""

						i = 0		# To count members in group.
						for tempMemberID in group['lights']:
							if i > 0:
								groupMemberIDs = groupMemberIDs + ", " + str(tempMemberID)
							else:
								groupMemberIDs = tempMemberID
							i += 1
						# Clear the "i" variable.
						del i

						#   Value manipulation.
						# Convert brightness from 0-255 range to 0-100 range.
						brightnessLevel = int(round(brightness / 255.0 * 100.0))
						# Compensate for incorrect rounding to zero if original brightness is not zero.
						if brightnessLevel == 0 and brightness > 0:
							brightnessLevel = 1
						# If the "on" state is False, it doesn't matter what brightness the hub
						#   is reporting, the effective brightness is zero.
						if onState == False:
							brightnessLevel = 0
						# Convert from HSB to RGB, scaling the hue and saturation values appropriately.
						hsb = HSVColor(hue / 182.0, saturation / 255.0, brightness / 255.0)
						rgb = hsb.convert_to('rgb', rgb_type='wide_gamut_rgb')
						colorRed = int(round(rgb.rgb_r))
						colorGreen = int(round(rgb.rgb_g))
						colorBlue = int(round(rgb.rgb_b))
						# Convert saturation from 0-255 scale to 0-100 scale.
						saturation = int(round(saturation / 255.0 * 100.0))
						# Convert hue from 0-65535 scale to 0-360 scale.
						hue = int(round(hue / 182.0))
						# Must first test color temp value. If it's zero, the formula throws a divide by zero execption.
						if colorTemp > 0:
							# Converting from mireds to Kelvin.
							colorTemp = int(round(1000000.0/colorTemp))
						else:
							colorTemp = 0

						#   Update Indigo states and properties common to all Hue devices.
						tempProps = device.pluginProps
						# Update the Hue group name.
						if nameOnHub != tempProps.get('nameOnHub', False):
							tempProps['nameOnHub'] = nameOnHub
							self.updateDeviceProps(device, tempProps)
						# Update the group type.
						if groupType != tempProps.get('type', False):
							tempProps['type'] = groupType
							self.updateDeviceProps(device, tempProps)
						# Update the group class.
						if groupClass != tempProps.get('groupClass', False):
							tempProps['groupClass'] = groupClass
							self.updateDeviceProps(device, tempProps)
						# Update the allOn state of the Hue group.
						self.updateDeviceState(device, 'allOn', allOn)
						# Update the anyOn state.
						self.updateDeviceState(device, 'anyOn', anyOn)
						# Update the alert state.
						self.updateDeviceState(device, 'alertMode', alert)
						# Update the effect state.
						self.updateDeviceState(device, 'effect', effect)
						# Update the group member IDs.
						self.updateDeviceState(device, 'groupMemberIDs', groupMemberIDs)

						# Update the Indigo device if the Hue group is on.
						if onState == True:
							# Update the brightness level if it's different.
							if device.states['brightnessLevel'] != brightnessLevel:
								# Log the update.
								indigo.server.log(u"\"" + device.name + "\" on to " + str(brightnessLevel), 'Updated')
								self.updateDeviceState(device, 'brightnessLevel', brightnessLevel)
							# Hue Degrees (0-360).
							self.updateDeviceState(device, 'hue', hue)
							# Saturation (0-100).
							self.updateDeviceState(device, 'saturation', saturation)
							# CIE XY Cromaticity.
							self.updateDeviceState(device, 'colorX', colorX)
							self.updateDeviceState(device, 'colorY', colorY)
							# Color Temperature (converted from 154-500 mireds to 6494-2000 K).
							self.updateDeviceState(device, 'colorTemp', colorTemp)
							# Color Mode.
							self.updateDeviceState(device, 'colorMode', colorMode)
							# Red, Green, Blue.
							self.updateDeviceState(device, 'colorRed', colorRed)
							self.updateDeviceState(device, 'colorGreen', colorGreen)
							self.updateDeviceState(device, 'colorBlue', colorBlue)

							### Update inherited states for Indigo 7+ devices.
							if "whiteLevel" in device.states or "redLevel" in device.states:
								# White Level (negative saturation, 0-100).
								self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
								# White Temperature (0-100).
								self.updateDeviceState(device, 'whiteTemperature', colorTemp)
								# Red, Green, Blue levels (0-100).
								self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
								self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
								self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))

						elif onState == False:
							# Hue group is off. Set brightness to zero.
							if device.states['brightnessLevel'] != 0:
								# Log the update.
								indigo.server.log(u"\"" + device.name + "\" off", 'Updated')
								self.updateDeviceState(device, 'brightnessLevel', 0)
							# Hue Degrees (convert from 0-65535 to 0-360).
							self.updateDeviceState(device, 'hue', hue)
							# Saturation (convert from 0-255 to 0-100).
							self.updateDeviceState(device, 'saturation', saturation)
							# CIE XY Cromaticity.
							self.updateDeviceState(device, 'colorX', colorX)
							self.updateDeviceState(device, 'colorY', colorY)
							# Color Temperature (convert from 154-500 mireds to 6494-2000 K).
							self.updateDeviceState(device, 'colorTemp', colorTemp)
							# Color Mode.
							self.updateDeviceState(device, 'colorMode', colorMode)
							# Red, Green, and Blue Color.
							#    If the bulb is off, all RGB values should be 0.
							self.updateDeviceState(device, 'colorRed', 0)
							self.updateDeviceState(device, 'colorGreen', 0)
							self.updateDeviceState(device, 'colorBlue', 0)
							# Effect
							self.updateDeviceState(device, 'effect', "")
							# Alert
							self.updateDeviceState(device, 'alertMode', "")

							### Update inherited states for Indigo 7+ devices.
							if "whiteLevel" in device.states or "redLevel" in device.states:
								# White Level (negative saturation, 0-100).
								self.updateDeviceState(device, 'whiteLevel', 100 - saturation)
								# White Temperature (0-100).
								self.updateDeviceState(device, 'whiteTemperature', colorTemp)
								# Red, Green, Blue levels (0-100).
								self.updateDeviceState(device, 'redLevel', int(round(colorRed / 255.0 * 100.0)))
								self.updateDeviceState(device, 'greenLevel', int(round(colorGreen / 255.0 * 100.0)))
								self.updateDeviceState(device, 'blueLevel', int(round(colorBlue / 255.0 * 100.0)))
						else:
							# Unrecognized on state, but not important enough to mention in regular log.
							self.debugLog(u"Hue group unrecognized on state given by hub: " + str(group['action']['on']))

						# Update any Hue Device Attribute Controller virtual dimmers associated with this bulb.
						for controlDeviceId in self.controlDeviceList:
							controlDevice = indigo.devices[int(controlDeviceId)]
							attributeToControl = controlDevice.pluginProps.get('attributeToControl', None)
							if deviceId == int(controlDevice.pluginProps.get('bulbDeviceId', None)):
								# Device has attributes controlled by a Hue Device Attribute Controler.
								#   Update the controller device based on current bulb device states.
								#   But if the control destination device is off, update the value of the
								#   controller (virtual dimmer) to 0.
								if device.onState == True:
									# Destination Hue Bulb device is on, update Attribute Controller brightness.
									if attributeToControl == "hue":
										# Convert hue scale from 0-360 to 0-100.
										self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(hue / 360.0 * 100.0)))
									elif attributeToControl == "saturation":
										self.updateDeviceState(controlDevice, 'brightnessLevel', saturation)
									elif attributeToControl == "colorRed":
										# Convert RGB scale from 0-255 to 0-100.
										self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorRed / 255.0 * 100.0)))
									elif attributeToControl == "colorGreen":
										# Convert RGB scale from 0-255 to 0-100.
										self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorGreen / 255.0 * 100.0)))
									elif attributeToControl == "colorBlue":
										# Convert RGB scale from 0-255 to 0-100.
										self.updateDeviceState(controlDevice, 'brightnessLevel', int(round(colorBlue / 255.0 * 100.0)))
									elif attributeToControl == "colorTemp":
										# Convert color temperature scale from 2000-6500 to 0-100.
										self.updateDeviceState(controlDevice, 'brightnessLevel', int(round((colorTemp - 2000.0) / 4500.0 * 100.0)))
								else:
									# Indigo Device is off.  Set Attribute Controller device brightness level to 0.
									self.updateDeviceState(controlDevice, 'brightnessLevel', 0)
						# End Hue Attribute Controller device updating.

						# Since only 1 Indigo device can control 1 Hue group, there's no need
						#    to continue the loop, so we're breaking out of the device matching loop.
						break

					# End check if this Hue Group device is the one associated with the Indigo device.
				# End loop through self.groupsDict.
			# End check if this is a Hue Group device.
		# End loop through self.deviceList.

	# Parse Hue Users (User Device) Data
	########################################
	def parseHueUsersData(self, hubDevice):
		self.debugLog(u"Starting parseHueUsersData.")
		# Soon to be filled in.

	# Parse Hue Scenes Data
	########################################
	def parseHueScenesData(self, hubDevice):
		self.debugLog(u"Starting parseHueScenesData.")
		# Soon to be filled in.



	# Turn Device On or Off
	########################################
	def doOnOff(self, device, onState, rampRate=-1):

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# onState:		Boolean on state.  True = on. False = off.
		# rampRate:		Optional float from 0 to 540.0 (higher values will probably work too).

		# If a rampRate wasn't specified (default of -1 assigned), use the default.
		#   (rampRate should be a float expressing transition time in seconds. Precission
		#   is limited to one-tenth seconds).
		if rampRate == -1:
			try:
				# Check for a blank default ramp rate.
				rampRate = device.pluginProps.get('rate', "")
				if rampRate == "":
					rampRate = 5
				else:
					# For user-friendliness, the rampRate provided in the device
					#   properties (as entered by the user) is expressed in fractions
					#   of a second (0.5 = 0.5 seconds, 10 = 10 seconds, etc), so
					#   it must be converted to 10th seconds here.
					rampRate = int(round(float(device.pluginProps['rate']) * 10))
			except Exception, e:
				errorText = u"Default ramp rate could not be obtained: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = 5
		else:
			# Convert the passed rampRate from seconds to 1/10th-seconds.
			rampRate = int(round(float(rampRate) * 10))

		# Get the current brightness. Range is 0-100.
		currentBrightness = int(device.states['brightnessLevel'])
		# Get the bulb's saved brightness (if it exists). Range is 1-255.
		savedBrightness = device.pluginProps.get('savedBrightness', 255)
		# If savedBrightness is not a number, try to make it into one.
		try:
			savedBrightness = int(savedBrightness)
		except ValueError:
			# It's not a string representation of a number, so just give it a number.
			savedBrightness = 255
		# Get the bulb's default brightness (if it exists). Range is 1-100.
		defaultBrightness = device.pluginProps.get('defaultBrightness', 0)
		# Make sure the defaultBrightness is valid.
		try:
			defaultBrightness = int(defaultBrightness)
		except ValueError:
			defaultBrightness = 0
		# If the bulb has a default brightness, use it instead of the saved brightness.
		if defaultBrightness > 0:
			# Convert default brightness from percentage to 1-255 range.
			savedBrightness = int(round(defaultBrightness / 100.0 * 255.0))
		# If the currentBrightness is less than 100% and is the same as the savedBrightness, go to 100%
		if currentBrightness < 100 and currentBrightness == int(round(savedBrightness / 255.0 * 100.0)):
			savedBrightness = 255

		# Sanity check for an IP address
		if hubDevice.pluginProps.get("address", None) is None:
			errorText = u"No IP address set for the Hue hub. You can get this information from the My Settings page at http://www.meethue.com"
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# If the requested onState is True (on), then use the
		#   saved brightness level (which was determined above).
		if onState == True:
			# If the bulb's saved brightness is zero or less (for some reason), use a default value of 100% on (255).
			if savedBrightness <= 0:
				savedBrightness = 255
			# Create the JSON object and send the command to the hub.
			requestData = json.dumps({"bri": savedBrightness, "on": onState, "transitiontime": rampRate})
			# Create the command based on whether this is a light or group device.
			if device.deviceTypeId == "hueGroup":
				command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
			else:
				command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog("Sending URL request: " + command)
			try:
				r = requests.put(command, data=requestData, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog("Got response - %s" % r.content)
			# Log the change.
			tempBrightness = int(round(savedBrightness / 255.0 * 100.0))
			# Compensate for rounding to zero.
			if tempBrightness == 0:
				tempBrightness = 1
			indigo.server.log(u"\"" + device.name + u"\" on to " + str(tempBrightness) + u" at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Update the Indigo device.
			self.updateDeviceState(device, 'brightnessLevel', tempBrightness)
		else:
			# Bulb is being turned off.
			# If the current brightness is lower than 6%, use a ramp rate of 0
			#   because dimming from that low of a brightness level to 0 isn't noticeable.
			if currentBrightness < 6:
				rampRate = 0
			# Create the JSON object and send the command to the hub.
			requestData = json.dumps({"on": onState, "transitiontime": rampRate})
			# Create the command based on whether this is a light or group device.
			if device.deviceTypeId == "hueGroup":
				command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
			else:
				command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.put(command, data=requestData, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Got response - %s" % r.content)
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" off at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Update the Indigo device.
			self.updateDeviceState(device, 'brightnessLevel', 0)

	# Set Brightness
	########################################
	def doBrightness(self, device, brightness, rampRate=-1, showLog=True):
		# brightness:	Integer from 0 to 255.
		# rampRate:		Optional float from 0 to 540.0 (higher values will probably work too).
		# showLog:		Optional boolean. False = hide change from Indigo log.

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# If a rampRate wasn't specified (default of -1 assigned), use the default.
		#   (rampRate should be a float expressing transition time in seconds. Precission
		#   is limited to one-tenth seconds.
		if rampRate == -1:
			try:
				# Check for a blank default ramp rate.
				rampRate = device.pluginProps.get('rate', "")
				if rampRate == "":
					rampRate = 5
				else:
					# For user-friendliness, the rampRate provided in the device
					#   properties (as entered by the user) is expressed in fractions
					#   of a second (0.5 = 0.5 seconds, 10 = 10 seconds, etc), so
					#   it must be converted to 10th seconds here.
					rampRate = int(round(float(device.pluginProps['rate']) * 10))
			except Exception, e:
				errorText = u"Default ramp rate could not be obtained: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = 5
		else:
			rampRate = int(round(float(rampRate) * 10))

		# Get the current brightness level.
		currentBrightness = device.states.get('brightnessLevel', 100)

		# Sanity check for an IP address
		ipAddress = hubDevice.pluginProps.get('address', None)
		if ipAddress is None:
			errorText = u"No IP address set for the Hue hub '%s'. You can get this information from the My Settings page at http://www.meethue.com" % (hubDevice.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# If requested brightness is greater than 0, proceed. Otherwise, turn off the bulb.
		if brightness > 0:
			requestData = json.dumps({"bri": int(brightness), "on": True, "transitiontime": rampRate})
			# Create the command based on whether this is a light or group device.
			if device.deviceTypeId == "hueGroup":
				command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
			else:
				command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog("Sending URL request: " + command)
			try:
				r = requests.put(command, data=requestData, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog("Got response - %s" % r.content)
			# Log the change.
			tempBrightness = int(round(brightness / 255.0 * 100.0))
			# Compensate for rounding to zero.
			if tempBrightness == 0:
				tempBrightness = 1
			# Only log changes if we're supposed to.
			if showLog:
				indigo.server.log(u"\"" + device.name + u"\" on to " + str(tempBrightness) + u" at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Update the device brightness (which automatically changes on state).
			self.updateDeviceState(device, 'brightnessLevel', int(tempBrightness))
		else:
			# Requested brightness is 0 (off).
			# If the current brightness is lower than 6%, use a ramp rate of 0
			#   because dimming from that low of a brightness level to 0 isn't noticeable.
			if currentBrightness < 6:
				rampRate = 0
			# Create the JSON request.
			requestData = json.dumps({"transitiontime": rampRate, "on": False})
			# Create the command based on whether this is a light or group device.
			if device.deviceTypeId == "hueGroup":
				command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
			else:
				command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
			self.debugLog(u"Sending URL request: " + command)
			try:
				r = requests.put(command, data=requestData, timeout=kTimeout)
			except requests.exceptions.Timeout:
				errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			except requests.exceptions.ConnectionError:
				errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
				# Don't display the error if it's been displayed already.
				if errorText != self.lastErrorMessage:
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
				return
			self.debugLog(u"Got response - %s" % r.content)
			# Log the change.
			if showLog:
				indigo.server.log(u"\"" + device.name + u"\" off at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Update the device brightness (which automatically changes on state).
			self.updateDeviceState(device, 'brightnessLevel', 0)

	# Set RGB Levels
	########################################
	def doRGB(self, device, red, green, blue, rampRate=-1):
		self.debugLog(u"doRGB called. RGB: %s, %s, %s. Device: %s" % (red, green, blue, device))
		# red:			Integer from 0 to 255.
		# green:		Integer from 0 to 255.
		# blue:			Integer from 0 to 255.
		# rampRate:		Optional float from 0 to 540.0 (higher values will probably work too).

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# Get the model ID of the device.
		modelId = device.pluginProps.get('modelId', "")

		# If a rampRate wasn't specified (default of -1 assigned), use the default.
		#   (rampRate should be a float expressing transition time in seconds. Precission
		#   is limited to one-tenth seconds.
		if rampRate == -1:
			try:
				# Check for a blank default ramp rate.
				rampRate = device.pluginProps.get('rate', "")
				if rampRate == "":
					rampRate = 5
				else:
					# For user-friendliness, the rampRate provided in the device
					#   properties (as entered by the user) is expressed in fractions
					#   of a second (0.5 = 0.5 seconds, 10 = 10 seconds, etc), so
					#   it must be converted to 10th seconds here.
					rampRate = int(round(float(device.pluginProps['rate']) * 10))
			except Exception, e:
				errorText = u"Default ramp rate could not be obtained: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = 5
		else:
			rampRate = int(round(float(rampRate) * 10))

		# Get the current brightness.
		currentBrightness = device.states.get('brightnessLevel', 100)

		# Convert RGB to HSL (same as HSB)
		rgb = RGBColor(red, green, blue, rgb_type='wide_gamut_rgb')
		hsb = rgb.convert_to('hsv')
		# Convert hue, saturation, and brightness to Hue system compatible ranges
		hue = int(round(hsb.hsv_h * 182.0))
		saturation = int(round(hsb.hsv_s * 255.0))
		brightness = int(round(hsb.hsv_v * 255.0))

		# Sanity check for an IP address
		if hubDevice.pluginProps.get("address", None) is None:
			errorText = u"No IP address set for the Hue hub. You can get this information from the My Settings page at http://www.meethue.com"
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Make sure the device is capable of rendering color.
		if modelId not in kHueBulbDeviceIDs and modelId not in kLightStripsDeviceIDs and modelId not in kLivingColorsDeviceIDs and device.deviceTypeId != "hueGroup":
			errorText = u"Cannot set RGB values. The \"%s\" device does not support color." % (device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Send to Hue (Create JSON request based on whether brightness is zero or not).
		if brightness > 0:
			requestData = json.dumps({"bri": brightness, "colormode": 'hs', "hue": hue, "sat": saturation, "transitiontime": int(rampRate), "on": True})
		else:
			# If the current brightness is below 6%, set the ramp rate to 0.
			if currentBrightness < 6:
				rampRate = 0
			# We create a separate command for when brightness is 0 (or below) because if
			#   the "on" state in the request was True, the Hue light wouldn't turn off.
			#   We also explicity state the X and Y values (equivilant to RGB of 1, 1, 1)
			#   because the xyy object contains invalid "NaN" values when all RGB values are 0.
			requestData = json.dumps({"bri": 0, "colormode": 'hs', "hue": 0, "sat": 0, "transitiontime": int(rampRate), "on": False})

		# Create the HTTP command and send it to the hub.
		# Create the command based on whether this is a light or group device.
		if device.deviceTypeId == "hueGroup":
			command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
		else:
			command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
		self.debugLog(u"Data: " + str(requestData) + u", URL: " + command)
		try:
			r = requests.put(command, data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		self.debugLog(u"Got response - %s" % r.content)

		# Update on Indigo
		if brightness > 0:
			# Convert brightness to a percentage.
			brightness = int(round(brightness / 255.0 * 100.0))
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" on to " + str(brightness) + u" with RGB values " + str(red) + u", " + str(green) + u" and " + str(blue) + u" at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Update the device state.
			self.updateDeviceState(device, 'brightnessLevel', brightness)
		else:
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" off at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Update the device state.
			self.updateDeviceState(device, 'brightnessLevel', 0)
		# Update the other device states.
		self.updateDeviceState(device, 'colorMode', "hs")
		self.updateDeviceState(device, 'hue', hue)
		self.updateDeviceState(device, 'saturation', saturation)
		# We don't set the colorRed, colorGreen, and colorBlue states
		#   because Hue devices are not capable of the full RGB color
		#   gamut and when the Hue hub updates the HSB values to reflect
		#   actual displayed light, the interpreted RGB values will not
		#   match the values entered by the user in the Action dialog.

	# Set Hue, Saturation and Brightness
	########################################
	def doHSB(self, device, hue, saturation, brightness, rampRate=-1):
		# hue:			Integer from 0 to 65535.
		# saturation:	Integer from 0 to 255.
		# brightness:	Integer from 0 to 255.
		# rampRate:		Optional float from 0 to 540.0 (higher values will probably work too).

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# If a rampRate wasn't specified (default of -1 assigned), use the default.
		#   (rampRate should be a float expressing transition time in seconds. Precission
		#   is limited to one-tenth seconds.
		if rampRate == -1:
			try:
				# Check for a blank default ramp rate.
				rampRate = device.pluginProps.get('rate', "")
				if rampRate == "":
					rampRate = 5
				else:
					# For user-friendliness, the rampRate provided in the device
					#   properties (as entered by the user) is expressed in fractions
					#   of a second (0.5 = 0.5 seconds, 10 = 10 seconds, etc), so
					#   it must be converted to 10th seconds here.
					rampRate = int(round(float(device.pluginProps['rate']) * 10))
			except Exception, e:
				errorText = u"Default ramp rate could not be obtained: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = 5
		else:
			rampRate = int(round(float(rampRate) * 10.0))

		# Get the current brightness level.
		currentBrightness = device.states.get('brightnessLevel', 100)

		# Sanity check for an IP address
		if hubDevice.pluginProps.get("address", None) is None:
			errorText = u"No IP address set for the Hue hub. You can get this information from the My Settings page at http://www.meethue.com"
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Make sure this device supports color.
		modelId = device.pluginProps.get('modelId', "")
		if modelId in kLivingWhitesDeviceIDs:
			errorText = u"Cannot set HSB values. The \"%s\" device does not support color." % (device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# If the current brightness is below 6% and the requested brightness is
		#   greater than 0, set the ramp rate to 0.
		if currentBrightness < 6 and brightness == 0:
			rampRate = 0

		# Send to Hue (Create JSON request based on whether brightness is zero or not).
		if brightness > 0:
			requestData = json.dumps({"bri":brightness, "colormode": 'hs', "hue":hue, "sat":saturation, "on":True, "transitiontime":rampRate})
		else:
			requestData = json.dumps({"bri":brightness, "colormode": 'hs', "hue":hue, "sat":saturation, "on":False, "transitiontime":rampRate})

		# Create the command based on whether this is a light or group device.
		if device.deviceTypeId == "hueGroup":
			command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
		else:
			command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
		self.debugLog(u"Request is %s" % requestData)
		try:
			r = requests.put(command, data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		self.debugLog(u"Got response - %s" % r.content)

		# Update on Indigo
		if int(round(brightness/255.0*100.0)) > 0:
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" on to " + str(int(round(brightness / 255.0 * 100.0))) + u" with hue " + str(int(round(hue / 182.0))) + u"° saturation " + str(int(round(saturation / 255.0 * 100.0))) + u"% at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Change the Indigo device.
			self.updateDeviceState(device, 'brightnessLevel', int(round(brightness / 255.0 * 100.0)))
		else:
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" off at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Change the Indigo device.
			self.updateDeviceState(device, 'brightnessLevel', 0)
		# Update the other device states.
		self.updateDeviceState(device, 'colorMode', "hs")
		self.updateDeviceState(device, 'hue', int(round(hue / 182.0)))
		self.updateDeviceState(device, 'saturation', int(saturation / 255.0 * 100.0))

	# Set CIE 1939 xyY Values
	########################################
	def doXYY(self, device, colorX, colorY, brightness, rampRate=-1):
		# colorX:		Integer from 0 to 1.0.
		# colorY:		Integer from 0 to 1.0.
		# brightness:	Integer from 0 to 255.
		# rampRate:		Optional float from 0 to 540.0 (higher values will probably work too).

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# If a rampRate wasn't specified (default of -1 assigned), use the default.
		#   (rampRate should be a float expressing transition time in seconds. Precission
		#   is limited to one-tenth seconds.
		if rampRate == -1:
			try:
				# Check for a blank default ramp rate.
				rampRate = device.pluginProps.get('rate', "")
				if rampRate == "":
					rampRate = 5
				else:
					# For user-friendliness, the rampRate provided in the device
					#   properties (as entered by the user) is expressed in fractions
					#   of a second (0.5 = 0.5 seconds, 10 = 10 seconds, etc), so
					#   it must be converted to 10th seconds here.
					rampRate = int(round(float(device.pluginProps['rate']) * 10))
			except Exception, e:
				errorText = u"Default ramp rate could not be obtained: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = 5
		else:
			rampRate = int(round(float(rampRate) * 10.0))

		# Get the current brightness level.
		currentBrightness = device.states.get('brightnessLevel', 100)

		# Sanity check for an IP address
		if hubDevice.pluginProps.get("address", None) is None:
			errorText = u"No IP address set for the Hue hub. You can get this information from the My Settings page at http://www.meethue.com"
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Make sure this device supports color.
		modelId = device.pluginProps.get('modelId', "")
		if modelId in kLivingWhitesDeviceIDs:
			errorText = u"Cannot set xyY values. The \"%s\" device does not support color." % (device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Make sure the X and Y values are sane.
		if colorX < 0 or colorX > 1:
			errorText = u"The specified X chromatisety value \"%s\" for the \"%s\" device is outside the acceptable range of 0.0 to 1.0." % (colorX, device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return
		if colorY < 0 or colorY > 1:
			errorText = u"The specified Y chromatisety value \"%s\" for the \"%s\" device is outside the acceptable range of 0.0 to 1.0." % (colorX, device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# If the current brightness is below 6% and the requested brightness is
		#   greater than 0, set the ramp rate to 0.
		if currentBrightness < 6 and brightness == 0:
			rampRate = 0

		# Send to Hue (Create JSON request based on whether brightness is zero or not).
		if brightness > 0:
			requestData = json.dumps({"bri":brightness, "colormode": 'xy', "xy":[colorX, colorY], "on":True, "transitiontime":rampRate})
		else:
			requestData = json.dumps({"bri":brightness, "colormode": 'xy', "xy":[colorX, colorY], "on":False, "transitiontime":rampRate})

		# Create the command based on whether this is a light or group device.
		if device.deviceTypeId == "hueGroup":
			command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
		else:
			command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
		self.debugLog(u"Request is %s" % requestData)
		try:
			r = requests.put(command, data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		self.debugLog(u"Got response - %s" % r.content)

		# Update on Indigo
		if int(round(brightness/255.0*100.0)) > 0:
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" on to " + str(int(round(brightness / 255.0 * 100.0))) + u" with x/y chromatisety values of " + str(round(colorX, 4)) + u"/" + str(round(colorY, 4)) + u" at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Change the Indigo device.
			self.updateDeviceState(device, 'brightnessLevel', int(round(brightness / 255.0 * 100.0)))
		else:
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" off at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			# Change the Indigo device.
			self.updateDeviceState(device, 'brightnessLevel', 0)
		# Update the other device states.
		self.updateDeviceState(device, 'colorMode', "xy")
		self.updateDeviceState(device, 'colorX', int(round(colorX, 4)))
		self.updateDeviceState(device, 'colorY', int(round(colorY, 4)))

	# Set Color Temperature
	########################################
	def doColorTemperature(self, device, temperature, brightness, rampRate=-1):
		# temperature:	Integer from 2000 to 6500.
		# brightness:	Integer from 0 to 255.
		# rampRate:		Optional float from 0 to 540.0 (higher values will probably work too).

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# If a rampRate wasn't specified (default of -1 assigned), use the default.
		#   (rampRate should be a float expressing transition time in seconds. Precission
		#   is limited to one-tenth seconds.
		if rampRate == -1:
			try:
				# Check for a blank default ramp rate.
				rampRate = device.pluginProps.get('rate', "")
				if rampRate == "":
					rampRate = 5
				else:
					# For user-friendliness, the rampRate provided in the device
					#   properties (as entered by the user) is expressed in fractions
					#   of a second (0.5 = 0.5 seconds, 10 = 10 seconds, etc), so
					#   it must be converted to 10th seconds here.
					rampRate = int(round(float(device.pluginProps['rate']) * 10))
			except Exception, e:
				errorText = u"Default ramp rate could not be obtained: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = 5
		else:
			rampRate = int(round(float(rampRate) * 10))

		# Make sure the color temperature value is sane.
		if temperature < 2000 or temperature > 6500:
			errorText = u"Invalid color temperature value of %i. Color temperatures must be between 2000 and 6500 K." % temperature
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the current brightness level.
		currentBrightness = device.states.get('brightnessLevel', 100)

		# Save the submitted color temperature into another variable.
		colorTemp = temperature

		# Convert temperature from K to mireds.
		#   Use the ceil and add 3 to help compensate for Hue behavior that "rounds up" to
		#   the next highest compatible mired value for the device.
		temperature = int(3 + ceil(1000000.0 / temperature))

		# Sanity check for an IP address
		if hubDevice.pluginProps.get("address", None) is None:
			errorText = u"No IP address set for the Hue hub. You can get this information from the My Settings page at http://www.meethue.com"
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Make sure this device supports color.
		modelId = device.pluginProps.get('modelId', "")
		if modelId in kLivingWhitesDeviceIDs:
			errorText = u"Cannot set Color Temperature values. The \"%s\" device does not support variable color tmperature." % (device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# If the current brightness is below 6% and the requested
		#   brightness is 0, set the ramp rate to 0.
		if currentBrightness < 6 and brightness == 0:
			rampRate = 0

		# Send to Hue (Create JSON request based on whether brightness is zero or not).
		if brightness > 0:
			requestData = json.dumps({"bri": brightness, "colormode": 'ct', "ct": temperature, "on": True, "transitiontime": int(rampRate)})
		else:
			requestData = json.dumps({"bri": brightness, "colormode": 'ct', "ct": temperature, "on": False, "transitiontime": int(rampRate)})

		# Create the command based on whether this is a light or group device.
		if device.deviceTypeId == "hueGroup":
			command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
		else:
			command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
		self.debugLog(u"Request is %s" % requestData)
		try:
			r = requests.put(command, data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		self.debugLog(u"Got response - %s" % r.content)

		# Update on Indigo
		if brightness > 0:
			# Log the change.
			tempBrightness = int(round(brightness / 255.0 * 100.0))
			# Compensate for rounding errors where it rounds down even though brightness is > 0.
			if tempBrightness == 0 and brightness > 0:
				tempBrightness = 1
			# Use originally submitted color temperature in the log version.
			indigo.server.log(u"\"" + device.name + u"\" on to " + str(tempBrightness) + u" using color temperature " + str(colorTemp) + u" K at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			self.updateDeviceState(device, 'brightnessLevel', int(round(brightness / 255.0 * 100.0)))
		else:
			# Log the change.
			indigo.server.log(u"\"" + device.name + u"\" off at ramp rate " + str(rampRate / 10.0) + u" sec.", 'Sent Hue Lights')
			self.updateDeviceState(device, 'brightnessLevel', 0)
		# Update the color mode state.
		self.updateDeviceState(device, 'colorMode', "ct")
		# Update the color temperature state (it's in mireds now, convert to Kelvin).
		self.updateDeviceState(device, 'colorTemp', colorTemp)

	# Start Alert (Blinking)
	########################################
	def doAlert(self, device, alertType="lselect"):
		# alertType:	Optional string.  String options are:
		#					lselect		: Long alert (default if nothing specified)
		#					select		: Short alert
		#					none		: Stop any running alerts

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		requestData = json.dumps({"alert": alertType})
		# Create the command based on whether this is a light or group device.
		if device.deviceTypeId == "hueGroup":
			command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
		else:
			command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
		try:
			r = requests.put(command, data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		self.debugLog(u"Got response - %s" % r.content)

		# Log the change.
		if alertType == "select":
			indigo.server.log(u"\"" + device.name + u"\" start short alert blink.", 'Sent Hue Lights')
		elif alertType == "lselect":
			indigo.server.log(u"\"" + device.name + u"\" start long alert blink.", 'Sent Hue Lights')
		elif alertType == "none":
			indigo.server.log(u"\"" + device.name + u"\" stop alert blink.", 'Sent Hue Lights')
		# Update the device state.
		self.updateDeviceState(device, 'alertMode', alertType)

	# Set Effect Status
	########################################
	def doEffect(self, device, effect):
		# effect:		String specifying the effect to use.  Hue supported effects are:
		#					none		: Stop any current effect
		#					colorloop	: Cycle through all hues at current brightness/saturation.
		#				Other effects may be supported by Hue with future firmware updates.

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Submit to Hue
		requestData = json.dumps({"effect": effect})
		self.debugLog(u"Request is %s" % requestData)
		# Create the command based on whether this is a light or group device.
		if device.deviceTypeId == "hueGroup":
			command = "http://%s/api/%s/groups/%s/action" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], groupId)
		else:
			command = "http://%s/api/%s/lights/%s/state" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"], bulbId)
		self.debugLog(u"URL: " + command)
		try:
			r = requests.put(command, data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		self.debugLog(u"Got response - %s" % r.content)

		# Log the change.
		indigo.server.log(u"\"" + device.name + u"\" set effect to \"" + effect + u"\"", 'Sent Hue Lights')
		# Update the device state.
		self.updateDeviceState(device, 'effect', effect)


	# Get Entire Hue Hub Config
	########################################
	def getHueConfig(self, hubDevice):
		# This method obtains the entire configuration object from the Hue hub.  That
		#   object contains various Hue hub settings along with every paired light and
		#   sensor device, along with every group, scene, trigger rule, and schedule
		#   on the hub.  For this reason, this method should not be called frequently
		#   to avoid causing Hue hub performacne degredation.
		self.debugLog(u"Starting getHueConfig.")

		# Sanity check for an IP address
		ipAddress = hubDevice.pluginProps.get('address', None)
		if ipAddress is None:
			errorText = u"No IP address set for the Hue hub '%s'. You can get this information from the My Settings page at http://www.meethue.com." % (hubDevice.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Sanity check for a host ID
		hostId = hubDevice.pluginProps.get('hostId', None)
		if hostId is None:
			errorText = u"Hub '%s' is not paired" % (hubDevice.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the internal hub ID
		hubId = str(hubDevice.id)

		# Force a timeout
		socket.setdefaulttimeout(kTimeout)

		try:
			# Send the command and parse the response
			command = "http://%s/api/%s/" % (ipAddress, hostId)
			self.debugLog(u"Sending command to hub '%s': %s" % (hubDevice.name, command))
			r = requests.get(command, timeout=kTimeout)
			hueConfigResponseData = json.loads(r.content)
			self.debugLog(u"Got response %s" % hueConfigResponseData)

			# We should have a dictionary. If so, it's a Hue configuration response.
			if isinstance(hueConfigResponseData, dict):
				self.debugLog(u"Loaded entire Hue hub configuration - %s" % (hueConfigResponseData))

				# Load the entire configuration into one big dictionary object.
				self.hueConfigDict[hubId] = hueConfigResponseData
				# Now separate out the component objects into various dictionaries to
				#   be used by other methods in the plugin.
				self.lightsDict[hubId] = hueConfigResponseData.get('lights', dict())
				self.groupsDict[hubId] = hueConfigResponseData.get('groups', dict())
				self.resourcesDict[hubId] = hueConfigResponseData.get('resourcelinks', dict())
				self.sensorsDict[hubId]	= hueConfigResponseData.get('sensors', dict())
				self.usersDict[hubId] = hueConfigResponseData['config'].get('whitelist', dict())
				self.scenesDict[hubId] = hueConfigResponseData.get('scenes', dict())
				self.rulesDict[hubId] = hueConfigResponseData.get('rules', dict())
				self.schedulesDict[hubId] = hueConfigResponseData.get('schedules', dict())

				# Make sure the plugin knows it's actually paired now.
				pluginProps = hubDevice.pluginProps
				pluginProps["paired"] = True
				hubDevice.replacePluginPropsOnServer(pluginProps)

			elif isinstance(hueConfigResponseData, list):
				# Get the first item
				firstResponseItem = hueConfigResponseData[0]

				# Did we get an error?
				errorDict = firstResponseItem.get('error', None)
				if errorDict is not None:

					errorCode = errorDict.get('type', None)

					# Is this a link button not pressed error?
					if errorCode == 1:
						errorText = u"Not paired with the Hue hub. Press the middle button on the Hue hub, then press the Pair Now button in the Hue Lights Configuration window (Plugins menu)."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						pluginProps = hubDevice.pluginProps
						pluginProps["paired"] = False
						hubDevice.replacePluginPropsOnServer(pluginProps)

					else:
						errorText = u"Error #%i from Hue hub when getting the Hue hub configuraiton. Description is \"%s\"." % (errorCode, errorDict.get('description', u"(no description"))
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						pluginProps = hubDevice.pluginProps
						pluginProps["paired"] = False
						hubDevice.replacePluginPropsOnServer(pluginProps)

				else:
					indigo.server.log(u"Unexpected response from Hue hub (%s) when getting the Hue hub configuration!" % (hueConfigResponseData))

			else:
				indigo.server.log(u"Unexpected response from Hue hub (%s) when getting the Hue hub configuration!" % (hueConfigResponseData))

		except requests.exceptions.Timeout:
			errorText = u"Failed to load the configuration from the Hue hub at %s after %i seconds - check settings and retry." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText

		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected, turned on and the network settings are correct." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return

		except Exception, e:
			self.errorLog(u"Unable to obtain the configuration from the Hue hub." + str(e))

	# Update Lights List
	########################################
	def updateLightsList(self, hubDevice):
		self.debugLog(u"Starting updateLightsList.")

		# Must have a hub device!
		if hubDevice is None:
			self.errorLog("No hub device provided to updateLightsLight()")
			return

		# Get the lights dict for this hub
		hubLightsDict = self.lightsDict[str(hubDevice.id)]

		# Remember the current number of Hue lights to see if new ones have been added.
		lastLightsCount = len(hubLightsDict)

		# Force a timeout
		socket.setdefaulttimeout(kTimeout)

		try:
			# Parse the response
			command = "http://%s/api/%s/lights" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"])
			self.debugLog(u"Sending command to hub: %s" % command)
			r = requests.get(command, timeout=kTimeout)
			lightsListResponseData = json.loads(r.content)
			self.debugLog(u"Got response %s" % lightsListResponseData)

			# We should have a dictionary. If so, it's a light list
			if isinstance(lightsListResponseData, dict):
				self.debugLog(u"Loaded lights list - %s" % (lightsListResponseData))
				self.lightsDict[str(hubDevice.id)] = lightsListResponseData

				# See if there are more lights now than there were last time we checked.
				if len(lightsListResponseData) > lastLightsCount and lastLightsCount is not 0:
					lightsCountChange = len(self.lightsDict) - lastLightsCount
					if lightsCountChange == 1:
						indigo.server.log(u"%i new Hue light found and loaded. Be sure to create an Indigo device to control the new Hue light." % lightsCountChange)
					else:
						indigo.server.log(u"%i new Hue lights found and loaded. Be sure to create Indigo devices to control the new Hue lights." % lightsCountChange)
				elif len(lightsListResponseData) < lastLightsCount:
					lightsCountChange = lastLightsCount - len(self.lightsDict)
					if lightsCountChange == 1:
						indigo.server.log(u"%i Hue light removal was detected from the Hue hub. Check your Hue Lights Indigo devices. One of them may have been controlling the missing Hue lights." % lightsCountChange)
					else:
						indigo.server.log(u"%i Hue light removals were detected on the Hue hub. Check your Hue Lights Indigo devices. Some of them may have been controlling the missing Hue lights." % lightsCountChange)

				# Make sure the plugin knows it's actually paired now.
				self.paired = True

			elif isinstance(lightsListResponseData, list):
				# Get the first item
				firstResponseItem = lightsListResponseData[0]

				# Did we get an error?
				errorDict = firstResponseItem.get('error', None)
				if errorDict is not None:

					errorCode = errorDict.get('type', None)

					# Is this a link button not pressed error?
					if errorCode == 1:
						errorText = u"Not paired with the Hue hub. Press the middle button on the Hue hub, then press the Pair Now button in the Hue Lights Configuration window (Plugins menu)."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						self.paired = False

					else:
						errorText = u"Error #%i from Hue hub when loading available devices. Description is \"%s\"." % (errorCode, errorDict.get('description', u"(no description"))
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						self.paired = False

				else:
					indigo.server.log(u"Unexpected response from Hue hub (%s) when loading available devices!" % (lightsListResponseData))

			else:
				indigo.server.log(u"Unexpected response from Hue hub (%s) when loading available devices!" % (lightsListResponseData))

		except requests.exceptions.Timeout:
			errorText = u"Failed to load lights list from the Hue hub at %s after %i seconds - check settings and retry." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText

		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected, turned on and the network settings are correct." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return

		except Exception, e:
			errorText = u"Unable to obtain list of Hue lights from the hub '%s' - %s" % (hubDevice.name, str(e))
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText

	# Update Groups List
	########################################
	def updateGroupsList(self, hubDevice):
		self.debugLog(u"Starting updateGroupsList.")

		# Get the lights dict for this hub
		hubGroupsDict = self.groupsDict[str(hubDevice.id)]

		# Remember the current number of Hue groups to see if new ones have been added.
		lastGroupsCount = len(hubGroupsDict)

		# Force a timeout
		socket.setdefaulttimeout(kTimeout)

		try:
			# Parse the response
			command = "http://%s/api/%s/groups" % (hubDevice.pluginProps["address"], hubDevice.pluginProps["hostId"])
			self.debugLog(u"Sending command to hub: %s" % command)
			r = requests.get(command, timeout=kTimeout)
			groupsListResponseData = json.loads(r.content)
			self.debugLog(u"Got response %s" % groupsListResponseData)

			# We should have a dictionary. If so, it's a group list
			if isinstance(groupsListResponseData, dict):
				self.debugLog(u"Loaded groups list - %s" % (groupsListResponseData))
				self.groupsDict[str(hubDevice.id)] = groupsListResponseData

				# See if there are more groups now than there were last time we checked.
				if len(hubGroupsDict) > lastGroupsCount and lastGroupsCount is not 0:
					groupsCountChange = len(groupsListResponseData) - lastGroupsCount
					if groupsCountChange == 1:
						indigo.server.log(u"%i new Hue group found and loaded. Be sure to create an Indigo device to control the new Hue group." % groupsCountChange)
					else:
						indigo.server.log(u"%i new Hue groups found and loaded. Be sure to create Indigo devices to control the new Hue groups." % groupsCountChange)
				elif len(groupsListResponseData) < lastGroupsCount:
					groupsCountChange = lastGroupsCount - len(groupsListResponseData)
					if groupsCountChange == 1:
						indigo.server.log(u"%i less Hue group was found on the Hue hub. Check your Hue Lights Indigo devices. One of them may have been controlling the missing Hue group." % groupsCountChange)
					else:
						indigo.server.log(u"%i fewer Hue groups were found on the Hue hub. Check your Hue Lights Indigo devices. Some of them may have been controlling the missing Hue groups." % groupsCountChange)

				# Make sure the plugin knows it's actually paired now.
				if hubDevice.pluginProps.get("paired", False) == False:
					pluginProps = hubDevice.pluginProps
					pluginProps["paired"] = True
					hubDevice.replacePluginPropsOnServer(pluginProps)


			elif isinstance(groupsListResponseData, list):
				# Get the first item
				firstResponseItem = groupsListResponseData[0]

				# Did we get an error?
				errorDict = firstResponseItem.get('error', None)
				if errorDict is not None:

					errorCode = errorDict.get('type', None)

					# Is this a link button not pressed error?
					if errorCode == 1:
						errorText = u"Not paired with the Hue hub. Press the middle button on the Hue hub, then press the Pair Now button in the Hue Lights Configuration window (Plugins menu)."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						pluginProps = hubDevice.pluginProps
						pluginProps["paired"] = False
						hubDevice.replacePluginPropsOnServer(pluginProps)

					else:
						errorText = u"Error #%i from Hue hub when loading available groups. Description is \"%s\"." % (errorCode, errorDict.get('description', u"(no description"))
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						pluginProps = hubDevice.pluginProps
						pluginProps["paired"] = False
						hubDevice.replacePluginPropsOnServer(pluginProps)

				else:
					indigo.server.log(u"Unexpected response from Hue hub (%s) when loading available groups!" % (groupsListResponseData))

			else:
				indigo.server.log(u"Unexpected response from Hue hub (%s) when loading available groups!" % (groupsListResponseData))

		except requests.exceptions.Timeout:
			errorText = u"Failed to load groups list from the Hue hub at %s after %i seconds - check settings and retry." % (hubDevice.pluginProps["address"], kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText

		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected, turned on and the network settings are correct." % (hubDevice.pluginProps["address"])
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return

		except Exception, e:
			self.errorLog(u"Unable to obtain list of Hue groups from the hub." + str(e))

	# Update Lights and Groups List
	########################################
	def updateAllHueLists(self, hubDevice):

		# This function is generally only used as a callback method for the
		#    Plugins -> Hue Lights -> Reload Hue Hub Config menu item, but can
		#    be used to force a reload of everything from the Hue hub.
		# Sanity check for an IP address
		ipAddress = hubDevice.pluginProps.get('address', None)
		if ipAddress is None:
			errorText = u"No IP address set for the Hue hub '%s'. You can get this information from the My Settings page at http://www.meethue.com." % (hubDevice.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the entire configuration from the Hue hub.
		self.getHueConfig(hubDevice)

		# Now report the results.
		#
		# Lights list...
		lightsDict = self.lightsDict[str(hubDevice.id)]
		if len(lightsDict) == 1:
			indigo.server.log(u"Loaded %i light." % len(lightsDict))
		else:
			indigo.server.log(u"Loaded %i lights." % len(lightsDict))

		# Groups list...
		groupsDict = self.groupsDict[str(hubDevice.id)]
		if len(groupsDict) == 1:
			indigo.server.log(u"Loaded %i group." % len(groupsDict))
		else:
			indigo.server.log(u"Loaded %i groups." % len(groupsDict))

		# User devices list...
		#if len(self.usersDict) == 1:
		#	indigo.server.log(u"Loaded %i user device." % len(self.usersDict))
		#else:
		#	indigo.server.log(u"Loaded %i user devices." % len(self.usersDict))

		# Scenes list...
		scenesDict = self.scenesDict[str(hubDevice.id)]
		if len(scenesDict) == 1:
			indigo.server.log(u"Loaded %i scene." % len(scenesDict))
		else:
			indigo.server.log(u"Loaded %i scenes." % len(scenesDict))

		# Resource links list...
		#if len(self.resourcesDict) == 1:
		#	indigo.server.log(u"Loaded %i resource link." % len(self.resourcesDict))
		#else:
		#	indigo.server.log(u"Loaded %i resource links." % len(self.resourcesDict))

		# Trigger rules list...
		#if len(self.rulesDict) == 1:
		#	indigo.server.log(u"Loaded %i trigger rule." % len(self.rulesDict))
		#else:
		#	indigo.server.log(u"Loaded %i trigger rules." % len(self.rulesDict))

		# Schedules list...
		#if len(self.schedulesDict) == 1:
		#	indigo.server.log(u"Loaded %i schedule." % len(self.schedulesDict))
		#else:
		#	indigo.server.log(u"Loaded %i schedules." % len(self.schedulesDict))

		# Sensors list...
		#if len(self.sensorsDict) == 1:
		#	indigo.server.log(u"Loaded %i sensor." % len(self.sensorsDict))
		#else:
		#	indigo.server.log(u"Loaded %i sensors." % len(self.sensorsDict))




	########################################
	# Hue Hub Pairing Methods
	########################################

	# Start/Restart Pairing with Hue Hub
	########################################
	def restartPairing(self, valuesDict, typeId, deviceId):
		# This method should only be used as a callback method from the
		#   hueHub device's configuration dialog "Pair Now" button.
		self.debugLog(u"Starting restartPairing.")
		isError = False
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = ""

		# Validate the IP Address field.
		if valuesDict.get('address', "") == "":
			# The field was left blank.
			self.debugLog(u"IP address \"%s\" is blank." % valuesDict['address'])
			isError = True
			errorsDict['address'] = u"The IP Address field is blank. Please enter an IP Address for the Hue hub."
			errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

		else:
			# The field wasn't blank. Check to see if the format is valid.
			try:
				# Try to format the IP Address as a 32-bit binary value. If this fails, the format was invalid.
				self.debugLog(u"Validating IP address \"%s\"." % valuesDict['address'])
				socket.inet_aton(valuesDict['address'])

			except socket.error:
				# IP Address format was invalid.
				self.debugLog(u"IP address format is invalid.")
				isError = True
				errorsDict['address'] = u"The IP Address is not valid. Please enter a valid IP address."
				errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

		# If there haven't been any errors so far, try to connect to the Hue hub to see
		#   if it's actually a Hue hub.
		if not isError:
			try:
				self.debugLog(u"Verifying that a Hue hub exists at IP address \"%s\"." %valuesDict['address'])
				command = "http://%s/description.xml" % valuesDict['address']
				self.debugLog(u"Accessing URL: %s" % command)
				r = requests.get(command, timeout=kTimeout)
				self.debugLog(u"Got response:\n%s" % r.content)

				# Quick and dirty check to see if this is a Philips Hue hub.
				if "Philips hue bridge" not in r.content:
					# If "Philips hue bridge" doesn't exist in the response, it's not a Hue hub.
					self.debugLog(u"No \"Philips hue bridge\" string found in response. This isn't a Hue hub.")
					isError = True
					errorsDict['address'] = u"This doesn't appear to be a Philips Hue hub.  Please verify the IP address."
					errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

				else:
					# This is likely a Hue hub.
					self.debugLog(u"Verified that this is a Hue hub.")

			except requests.exceptions.Timeout:
				errorText = u"Connection to %s timed out after %i seconds." % (valuesDict['address'], kTimeout)
				self.errorLog(errorText)
				isError = True
				errorsDict['address'] = u"Unable to reach the hub. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
				errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

			except requests.exceptions.ConnectionError:
				errorText = u"Connection to %s failed. There was a connection error." % valuesDict['address']
				self.errorLog(errorText)
				isError = True
				errorsDict['address'] = u"Connection error. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
				errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

			except Exception, e:
				errorText = u"Connection error. " + str(e)
				self.errorLog(errorText)
				isError = True
				errorsDict['address'] = u"Connection error. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
				errorsDict['showAlertText'] += errorsDict['address'] + u"\n\n"

		# Check for errors and act accordingly.
		if isError:
			# There was at least 1 error.
			errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
			return (valuesDict, errorsDict)
		else:
			# There weren't any errors, so...
			# Try pairing with the hub.

			# Configure timeout
			socket.setdefaulttimeout(kTimeout)

			# Request a username/key.
			try:
				indigo.server.log(u"Attempting to pair with the Hue hub at \"%s\"." % (valuesDict['address']))
				requestData = json.dumps({"devicetype": "Indigo Hue Lights"})
				self.debugLog(u"Request is %s" % requestData)
				command = "http://%s/api" % (valuesDict['address'])
				self.debugLog(u"Sending request to %s (via HTTP POST)." % command)
				r = requests.post(command, data=requestData, timeout=kTimeout)
				responseData = json.loads(r.content)
				self.debugLog(u"Got response %s" % responseData)

				# We should have a single response item
				if len(responseData) == 1:
					# Get the first item
					firstResponseItem = responseData[0]

					# See if we got an error.
					errorDict = firstResponseItem.get('error', None)
					if errorDict is not None:
						# We got an error.
						errorCode = errorDict.get('type', None)

						if errorCode == 101:
							# Center link button wasn't pressed on hub yet.
							errorText = u"Unable to pair with the Hue hub. Press the center button on the Hue hub, then click the \"Pair Now\" button."
							self.errorLog(errorText)
							isError = True
							errorsDict['startPairingButton'] = errorText
							errorsDict['showAlertText'] += errorsDict['startPairingButton'] + u"\n\n"

						else:
							errorText = u"Error #%i from the Hue hub. Description: \"%s\"." % (errorCode, errorDict.get('description', u"(No Description)"))
							self.errorLog(errorText)
							isError = True
							errorsDict['startPairingButton'] = errorText
							errorsDict['showAlertText'] += errorsDict['startPairingButton'] + u"\n\n"

					# See if we got a success response.
					successDict = firstResponseItem.get('success', None)
					if successDict is not None:
						# Pairing was successful.
						indigo.server.log(u"Paired with Hue hub successfully.")
						# The plugin was paired with the Hue hub.
						self.paired = True
						# Get the username provided by the hub.
						hueUsername = successDict['username']
						self.debugLog(u"Username (a.k.a. key) assigned by Hue hub to Hue Lights plugin: %s" % hueUsername)
						# Make sure the new username is returned to the config dialog.
						valuesDict['hostId'] = hueUsername

				else:
					# The Hue hub is acting weird.  There should have been only 1 response.
					errorText = u"Invalid response from Hue hub. Check the IP address and try again."
					self.errorLog(errorText)
					self.debugLog(u"Response from Hue hub contained %i items." % len(responseData))
					isError = True
					errorsDict['startPairingButton'] = errorText
					errorsDict['showAlertText'] += errorsDict['startPairingButton'] + u"\n\n"

			except requests.exceptions.Timeout:
				errorText = u"Connection to %s timed out after %i seconds." % (valuesDict['address'], kTimeout)
				self.errorLog(errorText)
				isError = True
				errorsDict['startPairingButton'] = u"Unable to reach the hub. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
				errorsDict['showAlertText'] += errorsDict['startPairingButton'] + u"\n\n"

			except requests.exceptions.ConnectionError:
				errorText = u"Connection to %s failed. There was a connection error." % valuesDict['address']
				self.errorLog(errorText)
				isError = True
				errorsDict['startPairingButton'] = u"Connection error. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
				errorsDict['showAlertText'] += errorsDict['startPairingButton'] + u"\n\n"

			except Exception, e:
				errorText = u"Connection error. " + str(e)
				self.errorLog(errorText)
				isError = True
				errorsDict['startPairingButton'] = u"Connection error. Please check the IP address and ensure that the Indigo server and Hue hub are connected to the network."
				errorsDict['showAlertText'] += errorsDict['startPairingButton'] + u"\n\n"

			# Check again for errors.
			if isError:
				# There was at least 1 error.
				errorsDict['showAlertText'] = errorsDict['showAlertText'].strip()
				return (valuesDict, errorsDict)
			else:
				# There still aren't any errors.
				return valuesDict


	########################################
	# Indigo UI Control Methods
	########################################

	# Dimmer/Relay Control Actions
	########################################
	def actionControlDimmerRelay(self, action, device):
		try:
			self.debugLog(u"actionControlDimmerRelay called for device " + device.name + u". action: " + str(action) + u"\n\ndevice: " + str(device))
		except Exception, e:
			self.debugLog(u"actionControlDimmerRelay called for device " + device.name + u". (Unable to display action or device data due to error: " + str(e) + u")")
		# Get the current brightness and on-state of the device.
		currentBrightness = device.states['brightnessLevel']
		currentOnState = device.states['onOffState']
		# Get key variables
		command = action.deviceAction

		# Get the hub device
		hubId = device.pluginProps.get("hubId", None)
		if hubId is None:
			self.errorLog("No hub configured for device '%s'" % (device.name))
			return
		hubDevice = indigo.devices.get(int(hubId), None)
		if hubDevice is None:
			self.errorLog("Failed to get hub with id '%i'" % (hubId))
			return

		# Act based on the type of device.
		#
		# -- Hue Bulbs --
		#
		if device.deviceTypeId == "hueBulb":
			bulbId = device.pluginProps.get('bulbId', None)
			self.debugLog(u"Command is %s, Bulb is %s" % (command, bulbId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it on.
				self.doOnOff(device, True)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it off by setting the brightness to minimum.
				self.doOnOff(device, False)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				if currentOnState == True:
					# It's on. Turn it off.
					self.doOnOff(device, False)
				else:
					# It's off. Turn it on.
					self.doOnOff(device, True)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = int(round(action.actionValue / 100.0 * 255.0))
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = brightnessLevel
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, brightnessLevel)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness + action.actionValue
				if brightnessLevel > 100:
					brightnessLevel = 100
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness - action.actionValue
				if brightnessLevel < 0:
					brightnessLevel = 0
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### SET COLOR LEVELS #####
			elif command == indigo.kDimmerRelayAction.SetColorLevels:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")

				actionColorVals = action.actionValue

				useRGB = False
				useHSB = False
				useColorTemp = False

				# The "Set RGBW Levels" action in Indigo 7.0 requires Red, Green, Blue and White leves, as well as
				#   White Temperature for devices that support both RGB and White levels (even if the device doesn't
				#   support simultaneous RGB and W settings).  We have to, therefor, make the assumption here that
				#   when the user sets the RGB and W levels all to 100 that they actually intend to use the White
				#   Temperature value for the action.  Alternatively, if they set the RGB levels to 100 but set a
				#   White level to something less than 100, we're assuming they intend to use the action to change
				#   the HSB saturation with the action and not RGB or color temperature.
				isGenericInterface = False
				if 'redLevel' in actionColorVals and 'greenLevel' in actionColorVals and 'blueLevel' in actionColorVals and 'whiteLevel' in actionColorVals and 'whiteTemperature' in actionColorVals:
					isGenericInterface = True
					if actionColorVals['redLevel'] == 100.0 and actionColorVals['greenLevel'] == 100.0 and actionColorVals['blueLevel'] == 100.0:
						useHSB = True
						if actionColorVals['whiteLevel'] == 100.0:
							useHSB = False
							useColorTemp = True
					else:
						useRGB = True

				# Construct a list of channel keys that are possible for what this device
				# supports. It may not support RGB or may not support white levels, for
				# example, depending on how the device's properties (SupportsColor, SupportsRGB,
				# SupportsWhite, SupportsTwoWhiteLevels, SupportsWhiteTemperature) have
				# been specified.
				channelKeys = []
				if device.supportsRGB:
					channelKeys.extend(['redLevel', 'greenLevel', 'blueLevel'])
				if device.supportsWhite:
					channelKeys.extend(['whiteLevel'])
				if device.supportsTwoWhiteLevels:
					channelKeys.extend(['whiteLevel2'])
				elif device.supportsWhiteTemperature:
					channelKeys.extend(['whiteTemperature'])
				redLevel = 0
				greenLevel = 0
				blueLevel = 0
				whiteLevel = 0
				colorTemp = 0

				# Enumerate through the possible color channels and extract each
				# value from the actionValue (actionColorVals).
				keyValueList = []
				for channel in channelKeys:
					if channel in actionColorVals:
						brightness = float(actionColorVals[channel])
						brightnessByte = int(round(255.0 * (brightness / 100.0)))

						if channel in device.states:
							if channel == "redLevel":
								redLevel = brightnessByte
								# Don't change the device action method selection if
								#   the action comes from the generic "Set RGBW Levels"
								#   Indigo 7 action.
								if not isGenericInterface:
									useRGB = True
							elif channel == "greenLevel":
								greenLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "blueLevel":
								blueLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "whiteLevel":
								# Indigo 7 has a "whiteLevel" parameter that is meaningless
								#   to the Hue system, so we're choosing to interpret "White level"
								#   to mean desaturation amount.
								whiteLevel = brightnessByte
								if not isGenericInterface:
									useHSB = True
							elif channel == "whiteTemperature":
								# The Indigo 7 interface allows users to select color temperature
								#   values over 6500 and (with Indigo 7.0) below 2000. Correct
								#   out of range values here.
								if brightness > 6500.0:
									brightness = 6500.0
								if brightness < 2000.0:
									brightness = 2000.0
								colorTemp = brightness
								if not isGenericInterface:
									useColorTemp = True

							keyValueList.append({'key':channel, 'value':brightness})

				# Tell the device to change based on which method we've decided to use.
				if useRGB:
					self.doRGB(device, redLevel, greenLevel, blueLevel)
				elif useHSB:
					# Indigo 7 has a "whiteLevel" parameter that is meaningless to the Hue system,
					#   so we're choosing to interpret "White level" to mean desaturation amount.
					#   Thus, we subtract the "whiteLevel" value from the full saturation value of 255.
					self.doHSB(device, int(round(65535.0 * (device.states['hue'] / 360.0))), 255 - whiteLevel, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))
				elif useColorTemp:
					self.doColorTemperature(device, colorTemp, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))

				# Tell the Indigo Server to update the color level states:
				if len(keyValueList) > 0:
					device.updateStatesOnServer(keyValueList)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled command \"%s\"" % (command))
			pass

		#
		# -- Hue Ambiance --
		#
		if device.deviceTypeId == "hueAmbiance":
			bulbId = device.pluginProps.get('bulbId', None)
			self.debugLog(u"Command is %s, Bulb is %s" % (command, bulbId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it on.
				self.doOnOff(device, True)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it off by setting the brightness to minimum.
				self.doOnOff(device, False)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				if currentOnState == True:
					# It's on. Turn it off.
					self.doOnOff(device, False)
				else:
					# It's off. Turn it on.
					self.doOnOff(device, True)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = int(round(action.actionValue / 100.0 * 255.0))
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = brightnessLevel
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, brightnessLevel)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness + action.actionValue
				if brightnessLevel > 100:
					brightnessLevel = 100
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness - action.actionValue
				if brightnessLevel < 0:
					brightnessLevel = 0
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### SET COLOR LEVELS #####
			elif command == indigo.kDimmerRelayAction.SetColorLevels:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")

				actionColorVals = action.actionValue

				useRGB = False
				useHSB = False
				useColorTemp = False

				isGenericInterface = False
				if 'redLevel' in actionColorVals and 'greenLevel' in actionColorVals and 'blueLevel' in actionColorVals and 'whiteLevel' in actionColorVals and 'whiteTemperature' in actionColorVals:
					isGenericInterface = True
					if actionColorVals['redLevel'] == 100.0 and actionColorVals['greenLevel'] == 100.0 and actionColorVals['blueLevel'] == 100.0:
						useHSB = True
						if actionColorVals['whiteLevel'] == 100.0:
							useHSB = False
							useColorTemp = True
					else:
						useRGB = True

				channelKeys = []
				if device.supportsRGB:
					channelKeys.extend(['redLevel', 'greenLevel', 'blueLevel'])
				if device.supportsWhite:
					channelKeys.extend(['whiteLevel'])
				if device.supportsTwoWhiteLevels:
					channelKeys.extend(['whiteLevel2'])
				elif device.supportsWhiteTemperature:
					channelKeys.extend(['whiteTemperature'])
				redLevel = 0
				greenLevel = 0
				blueLevel = 0
				whiteLevel = 0
				colorTemp = 0

				keyValueList = []
				for channel in channelKeys:
					if channel in actionColorVals:
						brightness = float(actionColorVals[channel])
						brightnessByte = int(round(255.0 * (brightness / 100.0)))

						if channel in device.states:
							if channel == "redLevel":
								redLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "greenLevel":
								greenLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "blueLevel":
								blueLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "whiteLevel":
								whiteLevel = brightnessByte
								if not isGenericInterface:
									useHSB = True
							elif channel == "whiteTemperature":
								if brightness > 6500.0:
									brightness = 6500.0
								if brightness < 2000.0:
									brightness = 2000.0
								colorTemp = brightness
								if not isGenericInterface:
									useColorTemp = True

							keyValueList.append({'key':channel, 'value':brightness})

				if useRGB:
					self.doRGB(device, redLevel, greenLevel, blueLevel)
				elif useHSB:
					self.doHSB(device, int(round(65535.0 * (device.states['hue'] / 360.0))), 255 - whiteLevel, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))
				elif useColorTemp:
					self.doColorTemperature(device, colorTemp, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))

				# Tell the Indigo Server to update the color level states:
				if len(keyValueList) > 0:
					device.updateStatesOnServer(keyValueList)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled command \"%s\"" % (command))
			pass

		#
		# -- LightStrips --
		#
		elif device.deviceTypeId == "hueLightStrips":
			bulbId = device.pluginProps.get('bulbId', None)
			self.debugLog(u"Command is %s, LightStrips device is %s" % (command, bulbId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it on.
				self.doOnOff(device, True)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it off by setting the brightness to minimum.
				self.doOnOff(device, False)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				if currentOnState == True:
					# It's on. Turn it off.
					self.doOnOff(device, False)
				else:
					# It's off. Turn it on.
					self.doOnOff(device, True)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = int(round(action.actionValue / 100.0 * 255.0))
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = brightnessLevel
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, brightnessLevel)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness + action.actionValue
				if brightnessLevel > 100:
					brightnessLevel = 100
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness - action.actionValue
				if brightnessLevel < 0:
					brightnessLevel = 0
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the device.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### SET COLOR LEVELS #####
			elif command == indigo.kDimmerRelayAction.SetColorLevels:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")

				actionColorVals = action.actionValue

				useRGB = False
				useHSB = False
				useColorTemp = False

				isGenericInterface = False
				if 'redLevel' in actionColorVals and 'greenLevel' in actionColorVals and 'blueLevel' in actionColorVals and 'whiteLevel' in actionColorVals and 'whiteTemperature' in actionColorVals:
					isGenericInterface = True
					if actionColorVals['redLevel'] == 100.0 and actionColorVals['greenLevel'] == 100.0 and actionColorVals['blueLevel'] == 100.0:
						useHSB = True
						if actionColorVals['whiteLevel'] == 100.0:
							useHSB = False
							useColorTemp = True
					else:
						useRGB = True

				channelKeys = []
				if device.supportsRGB:
					channelKeys.extend(['redLevel', 'greenLevel', 'blueLevel'])
				if device.supportsWhite:
					channelKeys.extend(['whiteLevel'])
				if device.supportsTwoWhiteLevels:
					channelKeys.extend(['whiteLevel2'])
				elif device.supportsWhiteTemperature:
					channelKeys.extend(['whiteTemperature'])
				redLevel = 0
				greenLevel = 0
				blueLevel = 0
				whiteLevel = 0
				colorTemp = 0

				keyValueList = []
				for channel in channelKeys:
					if channel in actionColorVals:
						brightness = float(actionColorVals[channel])
						brightnessByte = int(round(255.0 * (brightness / 100.0)))

						if channel in device.states:
							if channel == "redLevel":
								redLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "greenLevel":
								greenLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "blueLevel":
								blueLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "whiteLevel":
								whiteLevel = brightnessByte
								if not isGenericInterface:
									useHSB = True
							elif channel == "whiteTemperature":
								if brightness > 6500.0:
									brightness = 6500.0
								if brightness < 2000.0:
									brightness = 2000.0
								colorTemp = brightness
								if not isGenericInterface:
									useColorTemp = True

							keyValueList.append({'key':channel, 'value':brightness})

				if useRGB:
					self.doRGB(device, redLevel, greenLevel, blueLevel)
				elif useHSB:
					self.doHSB(device, int(round(65535.0 * (device.states['hue'] / 360.0))), 255 - whiteLevel, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))
				elif useColorTemp:
					self.doColorTemperature(device, colorTemp, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))

				# Tell the Indigo Server to update the color level states:
				if len(keyValueList) > 0:
					device.updateStatesOnServer(keyValueList)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled command \"%s\"" % (command))
			pass

		#
		# -- LivingColors Bloom --
		#
		elif device.deviceTypeId == "hueLivingColorsBloom":
			bulbId = device.pluginProps.get('bulbId', None)
			self.debugLog(u"Command is %s, LivingColors Bloom device is %s" % (command, bulbId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it on.
				self.doOnOff(device, True)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it off by setting the brightness to minimum.
				self.doOnOff(device, False)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				if currentOnState == True:
					# It's on. Turn it off.
					self.doOnOff(device, False)
				else:
					# It's off. Turn it on.
					self.doOnOff(device, True)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = int(round(action.actionValue / 100.0 * 255.0))
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = brightnessLevel
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, brightnessLevel)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness + action.actionValue
				if brightnessLevel > 100:
					brightnessLevel = 100
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness - action.actionValue
				if brightnessLevel < 0:
					brightnessLevel = 0
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the device.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### SET COLOR LEVELS #####
			elif command == indigo.kDimmerRelayAction.SetColorLevels:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")

				actionColorVals = action.actionValue

				useRGB = False
				useHSB = False
				useColorTemp = False

				isGenericInterface = False
				if 'redLevel' in actionColorVals and 'greenLevel' in actionColorVals and 'blueLevel' in actionColorVals and 'whiteLevel' in actionColorVals and 'whiteTemperature' in actionColorVals:
					isGenericInterface = True
					if actionColorVals['redLevel'] == 100.0 and actionColorVals['greenLevel'] == 100.0 and actionColorVals['blueLevel'] == 100.0:
						useHSB = True
						if actionColorVals['whiteLevel'] == 100.0:
							useHSB = False
							useColorTemp = True
					else:
						useRGB = True

				channelKeys = []
				if device.supportsRGB:
					channelKeys.extend(['redLevel', 'greenLevel', 'blueLevel'])
				if device.supportsWhite:
					channelKeys.extend(['whiteLevel'])
				if device.supportsTwoWhiteLevels:
					channelKeys.extend(['whiteLevel2'])
				elif device.supportsWhiteTemperature:
					channelKeys.extend(['whiteTemperature'])
				redLevel = 0
				greenLevel = 0
				blueLevel = 0
				whiteLevel = 0
				colorTemp = 0

				keyValueList = []
				for channel in channelKeys:
					if channel in actionColorVals:
						brightness = float(actionColorVals[channel])
						brightnessByte = int(round(255.0 * (brightness / 100.0)))

						if channel in device.states:
							if channel == "redLevel":
								redLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "greenLevel":
								greenLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "blueLevel":
								blueLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "whiteLevel":
								whiteLevel = brightnessByte
								if not isGenericInterface:
									useHSB = True
							elif channel == "whiteTemperature":
								if brightness > 6500.0:
									brightness = 6500.0
								if brightness < 2000.0:
									brightness = 2000.0
								colorTemp = brightness
								if not isGenericInterface:
									useColorTemp = True

							keyValueList.append({'key':channel, 'value':brightness})

				if useRGB:
					self.doRGB(device, redLevel, greenLevel, blueLevel)
				elif useHSB:
					self.doHSB(device, int(round(65535.0 * (device.states['hue'] / 360.0))), 255 - whiteLevel, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))
				elif useColorTemp:
					self.doColorTemperature(device, colorTemp, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))

				# Tell the Indigo Server to update the color level states:
				if len(keyValueList) > 0:
					device.updateStatesOnServer(keyValueList)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled command \"%s\"" % (command))
			pass

		#
		# -- LivingWhites --
		#
		elif device.deviceTypeId == "hueLivingWhites":
			bulbId = device.pluginProps.get('bulbId', None)
			self.debugLog(u"Command is %s, LivingWhites device is %s" % (command, bulbId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it on.
				self.doOnOff(device, True)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it off by setting the brightness to minimum.
				self.doOnOff(device, False)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				if currentOnState == True:
					# It's on. Turn it off.
					self.doOnOff(device, False)
				else:
					# It's off. Turn it on.
					self.doOnOff(device, True)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = int(round(action.actionValue / 100.0 * 255.0))
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = brightnessLevel
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, brightnessLevel)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness + action.actionValue
				if brightnessLevel > 100:
					brightnessLevel = 100
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness - action.actionValue
				if brightnessLevel < 0:
					brightnessLevel = 0
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the device.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### SET COLOR LEVELS #####
			elif command == indigo.kDimmerRelayAction.SetColorLevels:
				# This command should never be sent to this type of device because
				#   the LivingWhites devices shouldn't be defined as supporting color
				#   or variable color temperature.  But if, for some reason, they are,
				#   the code below should handle the call.
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")

				actionColorVals = action.actionValue

				useRGB = False
				useHSB = False
				useColorTemp = False

				isGenericInterface = False
				if 'redLevel' in actionColorVals and 'greenLevel' in actionColorVals and 'blueLevel' in actionColorVals and 'whiteLevel' in actionColorVals and 'whiteTemperature' in actionColorVals:
					isGenericInterface = True
					if actionColorVals['redLevel'] == 100.0 and actionColorVals['greenLevel'] == 100.0 and actionColorVals['blueLevel'] == 100.0:
						useHSB = True
						if actionColorVals['whiteLevel'] == 100.0:
							useHSB = False
							useColorTemp = True
					else:
						useRGB = True

				channelKeys = []
				if device.supportsRGB:
					channelKeys.extend(['redLevel', 'greenLevel', 'blueLevel'])
				if device.supportsWhite:
					channelKeys.extend(['whiteLevel'])
				if device.supportsTwoWhiteLevels:
					channelKeys.extend(['whiteLevel2'])
				elif device.supportsWhiteTemperature:
					channelKeys.extend(['whiteTemperature'])
				redLevel = 0
				greenLevel = 0
				blueLevel = 0
				whiteLevel = 0
				colorTemp = 0

				keyValueList = []
				for channel in channelKeys:
					if channel in actionColorVals:
						brightness = float(actionColorVals[channel])
						brightnessByte = int(round(255.0 * (brightness / 100.0)))

						if channel in device.states:
							if channel == "redLevel":
								redLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "greenLevel":
								greenLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "blueLevel":
								blueLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "whiteLevel":
								whiteLevel = brightnessByte
								if not isGenericInterface:
									useHSB = True
							elif channel == "whiteTemperature":
								if brightness > 6500.0:
									brightness = 6500.0
								if brightness < 2000.0:
									brightness = 2000.0
								colorTemp = brightness
								if not isGenericInterface:
									useColorTemp = True

							keyValueList.append({'key':channel, 'value':brightness})

				if useRGB:
					self.doRGB(device, redLevel, greenLevel, blueLevel)
				elif useHSB:
					self.doHSB(device, int(round(65535.0 * (device.states['hue'] / 360.0))), 255 - whiteLevel, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))
				elif useColorTemp:
					self.doColorTemperature(device, colorTemp, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))

				# Tell the Indigo Server to update the color level states:
				if len(keyValueList) > 0:
					device.updateStatesOnServer(keyValueList)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled command \"%s\"" % (command))
			pass

		#
		# -- Hue Group --
		#
		if device.deviceTypeId == "hueGroup":
			groupId = device.pluginProps.get('groupId', None)
			self.debugLog(u"Command is %s, Group is %s" % (command, groupId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it on.
				self.doOnOff(device, True)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Turn it off by setting the brightness to minimum.
				self.doOnOff(device, False)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				if currentOnState == True:
					# It's on. Turn it off.
					self.doOnOff(device, False)
				else:
					# It's off. Turn it on.
					self.doOnOff(device, True)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = int(round(action.actionValue / 100.0 * 255.0))
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = brightnessLevel
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, brightnessLevel)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness + action.actionValue
				if brightnessLevel > 100:
					brightnessLevel = 100
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				brightnessLevel = currentBrightness - action.actionValue
				if brightnessLevel < 0:
					brightnessLevel = 0
				# Save the new brightness level into the device properties.
				tempProps = device.pluginProps
				tempProps['savedBrightness'] = int(round(brightnessLevel / 100.0 * 255.0))
				self.updateDeviceProps(device, tempProps)
				# Set the new brightness level on the bulb.
				self.doBrightness(device, int(round(brightnessLevel / 100.0 * 255.0)))

			##### SET COLOR LEVELS #####
			elif command == indigo.kDimmerRelayAction.SetColorLevels:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")

				actionColorVals = action.actionValue

				useRGB = False
				useHSB = False
				useColorTemp = False

				isGenericInterface = False
				if 'redLevel' in actionColorVals and 'greenLevel' in actionColorVals and 'blueLevel' in actionColorVals and 'whiteLevel' in actionColorVals and 'whiteTemperature' in actionColorVals:
					isGenericInterface = True
					if actionColorVals['redLevel'] == 100.0 and actionColorVals['greenLevel'] == 100.0 and actionColorVals['blueLevel'] == 100.0:
						useHSB = True
						if actionColorVals['whiteLevel'] == 100.0:
							useHSB = False
							useColorTemp = True
					else:
						useRGB = True

				channelKeys = []
				if device.supportsRGB:
					channelKeys.extend(['redLevel', 'greenLevel', 'blueLevel'])
				if device.supportsWhite:
					channelKeys.extend(['whiteLevel'])
				if device.supportsTwoWhiteLevels:
					channelKeys.extend(['whiteLevel2'])
				elif device.supportsWhiteTemperature:
					channelKeys.extend(['whiteTemperature'])
				redLevel = 0
				greenLevel = 0
				blueLevel = 0
				whiteLevel = 0
				colorTemp = 0

				keyValueList = []
				for channel in channelKeys:
					if channel in actionColorVals:
						brightness = float(actionColorVals[channel])
						brightnessByte = int(round(255.0 * (brightness / 100.0)))

						if channel in device.states:
							if channel == "redLevel":
								redLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "greenLevel":
								greenLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "blueLevel":
								blueLevel = brightnessByte
								if not isGenericInterface:
									useRGB = True
							elif channel == "whiteLevel":
								whiteLevel = brightnessByte
								if not isGenericInterface:
									useHSB = True
							elif channel == "whiteTemperature":
								if brightness > 6500.0:
									brightness = 6500.0
								if brightness < 2000.0:
									brightness = 2000.0
								colorTemp = brightness
								if not isGenericInterface:
									useColorTemp = True

							keyValueList.append({'key':channel, 'value':brightness})

				if useRGB:
					self.doRGB(device, redLevel, greenLevel, blueLevel)
				elif useHSB:
					self.doHSB(device, int(round(65535.0 * (device.states['hue'] / 360.0))), 255 - whiteLevel, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))
				elif useColorTemp:
					self.doColorTemperature(device, colorTemp, int(round(255.0 * (device.states['brightnessLevel'] / 100.0))))

				# Tell the Indigo Server to update the color level states:
				if len(keyValueList) > 0:
					device.updateStatesOnServer(keyValueList)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				self.getGroupStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled command \"%s\"" % (command))
			pass

		#
		# -- Hue Attribute Controller --
		#
		elif device.deviceTypeId == "hueAttributeController":
			bulbDeviceId = device.pluginProps.get('bulbDeviceId', None)
			attributeToControl = device.pluginProps.get('attributeToControl', None)
			rate = device.pluginProps.get('rate', "")
			onLevel = device.pluginProps.get('defaultOnLevel', "")

			if bulbDeviceId == None:
				indigo.server.log(u"Hue Attribute Controller \"" + device.name + u"\" has no Hue Bulb device defined as the control destination. Action ignored.", isError=True)
				return None
			else:
				# Define the control destination device object and related variables.
				bulbDevice = indigo.devices[int(bulbDeviceId)]
				bulbDeviceProps = bulbDevice.pluginProps
				brightnessLevel = bulbDevice.states.get('brightnessLevel', 0)
				saturation = bulbDevice.states.get('saturation', 0)
				hue = bulbDevice.states.get('hue', 0)
				colorRed = bulbDevice.states.get('colorRed', 0)
				colorGreen = bulbDevice.states.get('colorGreen', 0)
				colorBlue = bulbDevice.states.get('colorBlue', 0)
				colorTemp = bulbDevice.states.get('colorTemp', 2000)
				# Convert attribute scales to work with the doHSB method.
				brightnessLevel = int(round(brightnessLevel / 100.0) * 255.0)
				saturation = int(round(saturation / 100.0 * 255.0))
				hue = int(hue * 182.0)

			if attributeToControl == None:
				errorText = u"Hue Attribute Controller \"" + device.name + u"\" has no Attribute to Control specified. Action ignored."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None

			if rate == "":
				# If a ramp rate wasn't specified, set to -1 to use default rate.
				rate = -1
			else:
				# If it was specified, make sure it's a number. If not, set to default.
				try:
					rate = float(rate)
					if rate < 0 or rate > 540:
						# If the rate is less than 0 or greater than 540, that's an invalid value. Use default.
						rate = -1
				except Exception, e:
					self.debugLog(u"Invalid rate value. Error: " + str(e))
					rate = -1

			if onLevel == "":
				# Default on level wasn't specified.  Use 100% as default.
				onLevel = 100
			else:
				# If it was specified, make sure it's a number. If not, set to 100% as default.
				try:
					onLevel = int(onLevel)
					if onLevel < 1 or onLevel > 100:
						# If the on level doesn't make sense, set it to 100%.
						onLevel = 100
				except Exception, e:
					onLevel = 100
			convertedOnLevel = onLevel

			self.debugLog(u"Command is %s, Bulb device ID is %s" % (command, bulbDeviceId))

			##### TURN ON #####
			if command == indigo.kDeviceAction.TurnOn:
				try:
					self.debugLog(u"device on:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device on: (Unable to display action data due to error: " + str(e) + ")")
				# Set the destination attribute to maximum.
				if attributeToControl == "hue":
					# Hue
					#   (65535 is the maximum value allowed by Hue and represents a hue of 360 degrees).
					# Convert onLevel to valid hue number.
					convertedOnLevel = int(onLevel / 100.0 * 360.0 * 182.0)
					self.doHSB(bulbDevice, convertedOnLevel, saturation, brightnessLevel, rate)
				elif attributeToControl == "saturation":
					# Saturation
					#   (255 is the maximum value allowed by Hue).
					# Convert onLevel to valid saturation number.
					convertedOnLevel = int(onLevel / 100.0 * 255.0)
					self.doHSB(bulbDevice, hue, convertedOnLevel, brightnessLevel, rate)
				elif attributeToControl == "colorRed":
					# RGB (Red)
					#   (255 is the maximum value allowed).
					# Convert onLevel to valid RGB number.
					convertedOnLevel = int(onLevel / 100.0 * 255.0)
					self.doRGB(bulbDevice, convertedOnLevel, colorGreen, colorBlue, rate)
				elif attributeToControl == "colorGreen":
					# RGB (Green)
					#   (255 is the maximum value allowed).
					# Convert onLevel to valid RGB number.
					convertedOnLevel = int(onLevel / 100.0 * 255.0)
					self.doRGB(bulbDevice, colorRed, convertedOnLevel, colorBlue, rate)
				elif attributeToControl == "colorBlue":
					# RGB (Blue)
					#   (255 is the maximum value allowed).
					# Convert onLevel to valid RGB number.
					convertedOnLevel = int(onLevel / 100.0 * 255.0)
					self.doRGB(bulbDevice, colorRed, colorGreen, convertedOnLevel, rate)
				elif attributeToControl == "colorTemp":
					# Color Temperature
					#   (6500 K is the highest value allowed).
					# Convert onLevel to valid color temperature number.
					convertedOnLevel = int(onLevel / 100.0 * 4500 + 2000)
					self.doColorTemperature(bulbDevice, convertedOnLevel, brightnessLevel, rate)
				# Update the virtual dimmer device.
				self.updateDeviceState(device, 'brightnessLevel', onLevel)

			##### TURN OFF #####
			elif command == indigo.kDeviceAction.TurnOff:
				try:
					self.debugLog(u"device off:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device off: (Unable to display action data due to error: " + str(e) + u")")
				# Set the destination attribute to minimum.
				if attributeToControl == "hue":
					# Hue
					#   (0 is the minimum value allowed by Hue and represents a hue of 0 degrees).
					self.doHSB(bulbDevice, 0, saturation, brightnessLevel, rate)
				elif attributeToControl == "saturation":
					# Saturation
					#   (0 is the minimum value allowed by Hue).
					self.doHSB(bulbDevice, hue, 0, brightnessLevel, rate)
				elif attributeToControl == "colorRed":
					# RGB (Red)
					#   (0 is the minimum value allowed).
					self.doRGB(bulbDevice, 0, colorGreen, colorBlue, rate)
				elif attributeToControl == "colorGreen":
					# RGB (Green)
					#   (0 is the minimum value allowed).
					self.doRGB(bulbDevice, colorRed, 0, colorBlue, rate)
				elif attributeToControl == "colorBlue":
					# RGB (Blue)
					#   (0 is the minimum value allowed).
					self.doRGB(bulbDevice, colorRed, colorGreen, 0, rate)
				elif attributeToControl == "colorTemp":
					# Color Temperature
					#   (2000 K is the lowest value allowed).
					self.doColorTemperature(bulbDevice, 2000, brightnessLevel, rate)
				# Update the virtual dimmer device.
				self.updateDeviceState(device, 'brightnessLevel', 0)

			##### TOGGLE #####
			elif command == indigo.kDeviceAction.Toggle:
				try:
					self.debugLog(u"device toggle:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device toggle: (Unable to display action due to error: " + str(e) + u")")
				# Set the destination attribute to either maximum or minimum.
				if attributeToControl == "hue":
					# Hue
					#   (0 or 65535)
					if currentOnState == True:
						# It's something other than 0. Turn it off by setting the value to minimum.
						self.doHSB(bulbDevice, 0, saturation, brightnessLevel, rate)
					else:
						# It's 0. Turn it on by setting the value to maximum.
						# Convert onLevel to valid hue number.
						convertedOnLevel = int(onLevel / 100.0 * 360.0 * 182.0)
						self.doHSB(bulbDevice, convertedOnLevel, saturation, brightnessLevel, rate)
				elif attributeToControl == "saturation":
					# Saturation
					#   (0 to 255)
					if currentOnState == True:
						# It's something other than 0. Turn it off by setting the value to minimum.
						self.doHSB(bulbDevice, hue, 0, brightnessLevel, rate)
					else:
						# It's 0. Turn it on by setting the value to maximum.
						# Convert onLevel to valid saturation number.
						convertedOnLevel = int(onLevel / 100.0 * 255.0)
						self.doHSB(bulbDevice, hue, convertedOnLevel, brightnessLevel, rate)
				elif attributeToControl == "colorRed":
					# RGB (Red)
					#   (0 to 255)
					if currentOnState == True:
						# It's something other than 0. Turn it off by setting the value to minimum.
						self.doRGB(bulbDevice, 0, colorGreen, colorBlue, rate)
					else:
						# It's 0. Turn it on by setting the value to maximum.
						# Convert onLevel to valid RGB number.
						convertedOnLevel = int(onLevel / 100.0 * 255.0)
						self.doRGB(bulbDevice, convertedOnLevel, colorGreen, colorBlue, rate)
				elif attributeToControl == "colorGreen":
					# RGB (Green)
					#   (0 to 255)
					if currentOnState == True:
						# It's something other than 0. Turn it off by setting the value to minimum.
						self.doRGB(bulbDevice, colorRed, 0, colorBlue, rate)
					else:
						# It's 0. Turn it on by setting the value to maximum.
						# Convert onLevel to valid RGB number.
						convertedOnLevel = int(onLevel / 100.0 * 255.0)
						self.doRGB(bulbDevice, colorGreen, convertedOnLevel, colorBlue, rate)
				elif attributeToControl == "colorBlue":
					# RGB (Blue)
					#   (0 to 255)
					if currentOnState == True:
						# It's something other than 0. Turn it off by setting the value to minimum.
						self.doRGB(bulbDevice, colorRed, colorGreen, 0, rate)
					else:
						# It's 0. Turn it on by setting the value to maximum.
						# Convert onLevel to valid RGB number.
						convertedOnLevel = int(onLevel / 100.0 * 255.0)
						self.doRGB(bulbDevice, colorRed, colorGreen, convertedOnLevel, rate)
				elif attributeToControl == "colorTemp":
					# Color Temperature
					#   (2000 to 6500)
					if currentOnState == True:
						# It's something other than 0. Turn it off by setting the value to minimum.
						self.doColorTemperature(bulbDevice, 2000, brightnessLevel, rate)
					else:
						# It's 0. Turn it on by setting the value to maximum.
						# Convert onLevel to valid color temperature number.
						convertedOnLevel = int(onLevel / 100.0 * 4500 + 2000)
						self.doColorTemperature(bulbDevice, convertedOnLevel, brightnessLevel, rate)
				# Update the virtual dimmer device.
				if currentOnState == True:
					self.updateDeviceState(device, 'brightnessLevel', 0)
				else:
					self.updateDeviceState(device, 'brightnessLevel', onLevel)

			##### SET BRIGHTNESS #####
			elif command == indigo.kDeviceAction.SetBrightness:
				try:
					self.debugLog(u"device set brightness:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device set brightness: (Unable to display action data due to error: " + str(e) + u")")
				# Set the destination attribute to maximum.
				if attributeToControl == "hue":
					# Hue
					#   (0 to 65535. actionValue will be in the range 0 to 100 though, so convert).
					self.doHSB(bulbDevice, int(round(action.actionValue / 100.0 * 360.0 * 182.0)), saturation, brightnessLevel, rate)
				elif attributeToControl == "saturation":
					# Saturation
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doHSB(bulbDevice, hue, int(round(action.actionValue / 100.0 * 255.0)), brightnessLevel, rate)
				elif attributeToControl == "colorRed":
					# RGB (Red)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, int(round(action.actionValue / 100.0 * 255.0)), colorGreen, colorBlue, rate)
				elif attributeToControl == "colorGreen":
					# RGB (Green)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, colorRed, int(round(action.actionValue / 100.0 * 255.0)), colorBlue, rate)
				elif attributeToControl == "colorBlue":
					# RGB (Blue)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, colorRed, colorGreen, int(round(action.actionValue / 100.0 * 255.0)), rate)
				elif attributeToControl == "colorTemp":
					# Color Temperature
					#   (2000 to 6500. actionValue will be in range 0 to 100 though, so convert).
					self.doColorTemperature(bulbDevice, int(round(action.actionValue / 100.0 * 4500.0 + 2000.0)), brightnessLevel, rate)
				# Update the virtual dimmer device.
				self.updateDeviceState(device, 'brightnessLevel', action.actionValue)

			##### BRIGHTEN BY #####
			elif command == indigo.kDeviceAction.BrightenBy:
				try:
					self.debugLog(u"device increase brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device increase brightness by: (Unable to display action data due to error: " + str(e) + u")")
				# Calculate the new brightness.
				newValue = currentBrightness + action.actionValue
				if newValue > 100:
					newValue = 100
				# Set the destination attribute to maximum.
				if attributeToControl == "hue":
					# Hue
					#   (0 to 65535. actionValue will be in the range 0 to 100 though, so convert).
					self.doHSB(bulbDevice, int(round(newValue / 100.0 * 360.0 * 182.0)), saturation, brightnessLevel, rate)
				elif attributeToControl == "saturation":
					# Saturation
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doHSB(bulbDevice, hue, int(round(newValue / 100.0 * 255.0)), brightnessLevel, rate)
				elif attributeToControl == "colorRed":
					# RGB (Red)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, int(round(newValue / 100.0 * 255.0)), colorGreen, colorBlue, rate)
				elif attributeToControl == "colorGreen":
					# RGB (Green)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, colorRed, int(round(newValue / 100.0 * 255.0)), colorBlue, rate)
				elif attributeToControl == "colorBlue":
					# RGB (Blue)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, colorRed, colorGreen, int(round(newValue / 100.0 * 255.0)), rate)
				elif attributeToControl == "colorTemp":
					# Color Temperature
					#   (2000 to 6500. actionValue will be in range 0 to 100 though, so convert).
					self.doColorTemperature(bulbDevice, int(round(newValue / 100.0 * 4500.0 + 2000.0)), brightnessLevel, rate)
				# Update the virtual dimmer device.
				self.updateDeviceState(device, 'brightnessLevel', newValue)

			##### DIM BY #####
			elif command == indigo.kDeviceAction.DimBy:
				try:
					self.debugLog(u"device decrease brightness by:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device decrease brightness by: (Unable to display action data due to error: " + str(e) + u")")
				# Calculate the new brightness.
				newValue = currentBrightness - action.actionValue
				if newValue < 0:
					newValue = 0
				# Set the destination attribute to maximum.
				if attributeToControl == "hue":
					# Hue
					#   (0 to 65535. actionValue will be in the range 0 to 100 though, so convert).
					self.doHSB(bulbDevice, int(round(newValue / 100.0 * 360.0 * 182.0)), saturation, brightnessLevel, rate)
				elif attributeToControl == "saturation":
					# Saturation
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doHSB(bulbDevice, hue, int(round(newValue / 100.0 * 255.0)), brightnessLevel, rate)
				elif attributeToControl == "colorRed":
					# RGB (Red)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, int(round(newValue / 100.0 * 255.0)), colorGreen, colorBlue, rate)
				elif attributeToControl == "colorGreen":
					# RGB (Green)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, colorRed, int(round(newValue / 100.0 * 255.0)), colorBlue, rate)
				elif attributeToControl == "colorBlue":
					# RGB (Blue)
					#   (0 to 255. actionValue will be in the range 0 to 100 though, so convert).
					self.doRGB(bulbDevice, colorRed, colorGreen, int(round(newValue / 100.0 * 255.0)), rate)
				elif attributeToControl == "colorTemp":
					# Color Temperature
					#   (2000 to 6500. actionValue will be in range 0 to 100 though, so convert).
					self.doColorTemperature(bulbDevice, int(round(newValue / 100.0 * 4500.0 + 2000.0)), brightnessLevel, rate)
				# Update the virtual dimmer device.
				self.updateDeviceState(device, 'brightnessLevel', newValue)

			##### REQUEST STATUS #####
			elif command == indigo.kDeviceAction.RequestStatus:
				try:
					self.debugLog(u"device request status:\n%s" % action)
				except Exception, e:
					self.debugLog(u"device request status: (Unable to display action data due to error: " + str(e) + u")")
				# This actually requests the status of the virtual dimmer device's destination Hue device/group.
				self.getBulbStatus(bulbDeviceId)
				# Show the current virtual dimmer level in the log.  There will likely be a delay for
				#   the destination Hue device status, so we're not going to wait for that status update.
				#   We'll just return the current virtual device brightness level in the log.
				indigo.server.log(u"\"" + device.name + u"\" status request (currently: " + str(currentBrightness) + u")")

			#### CATCH ALL #####
			else:
				indigo.server.log(u"Unhandled Hue Attribute Controller command \"%s\"" % (command))
			pass

	########################################
	# Action Handling Methods
	########################################

	# Recall Scene
	########################################
	def recallScene(self, action, device):

		# Catch no device
		if device == None:
			errorText = u"No device was selected for the \"" + action.name + u"\" action. Please edit the action and select a Hue Light device."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the scene ID
		sceneId = action.props.get("sceneId", None)
		if sceneId is None:
			errorText = u"No scene is selected to recall."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the address and host details
		ipAddress = device.pluginProps.get("address", None)
		hostId = device.pluginProps.get("hostId", None)

		# Send the recall request
		requestData = json.dumps({"scene": sceneId})
		self.debugLog("Sending scene request - %s" % requestData)
		try:
			r = requests.put("http://%s/api/%s/groups/0/action" % (ipAddress, hostId), data=requestData, timeout=kTimeout)
		except requests.exceptions.Timeout:
			errorText = u"Failed to connect to the Hue hub at %s after %i seconds. - Check that the hub is connected and turned on." % (
				ipAddress, kTimeout)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return
		except requests.exceptions.ConnectionError:
			errorText = u"Failed to connect to the Hue hub at %s. - Check that the hub is connected and turned on." % (
				ipAddress)
			# Don't display the error if it's been displayed already.
			if errorText != self.lastErrorMessage:
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
			return

	# Start/Stop Brightening
	########################################
	def startStopBrightening(self, action, device):
		# Catch if no device was passed in the action call.
		if device == None:
			errorText = u"No device was selected for the \"" + action.name + u"\" action. Please edit the action and select a Hue Light device."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		self.debugLog(u"startStopBrightening: device: " + device.name + u", action:\n" + str(action))
		# Make sure the device is in the deviceList.
		if device.id in self.deviceList:

			# First, remove from the dimmingList if it's there.
			if device.id in self.dimmingList:
				# Log the event to Indigo log.
				indigo.server.log(u"\"" + device.name + u"\" stop dimming", 'Sent Hue Lights')
				# Remove from list.
				self.dimmingList.remove(device.id)

			# Now remove from brighteningList if it's in the list and add if not.
			if device.id in self.brighteningList:
				# Log the event to Indigo log.
				indigo.server.log(u"\"" + device.name + u"\" stop brightening", 'Sent Hue Lights')
				# Remove from list.
				self.brighteningList.remove(device.id)
				# Get the bulb status
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + u")", 'Sent Hue Lights')
			else:
				# Only begin brightening if current brightness is less than 100%.
				if device.states['brightnessLevel'] < 100:
					# Log the event in Indigo log.
					indigo.server.log(u"\"" + device.name + u"\" start brightening", 'Sent Hue Lights')
					# Add to list.
					self.brighteningList.append(device.id)

		return

	# Start/Stop Dimming
	########################################
	def startStopDimming(self, action, device):
		# Catch if no device was passed in the action call.
		if device == None:
			errorText = u"No device was selected for the \"" + action.name + "\" action. Please edit the action and select a Hue Light device."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		self.debugLog(u"startStopDimming: device: " + device.name + ", action:\n" + str(action))
		# Make sure the device is in the deviceList.
		if device.id in self.deviceList:
			# First, remove from brighteningList if it's there.
			if device.id in self.brighteningList:
				# Log the event to Indigo log.
				indigo.server.log(u"\"" + device.name + u"\" stop brightening", 'Sent Hue Lights')
				# Remove from list.
				self.brighteningList.remove(device.id)

			# Now remove from dimmingList if it's in the list and add if not.
			if device.id in self.dimmingList:
				# Log the event to Indigo log.
				indigo.server.log(u"\"" + device.name + u"\" stop dimming", 'Sent Hue Lights')
				# Remove from list.
				self.dimmingList.remove(device.id)
				# Get the bulb status
				self.getBulbStatus(device.id)
				# Log the new brightnss.
				indigo.server.log(u"\"" + device.name + u"\" status request (received: " + str(device.states['brightnessLevel']) + ")", 'Sent Hue Lights')
			else:
				# Only begin dimming if current brightness is greater than 0%.
				if device.states['brightnessLevel'] > 0:
					# Log the event in Indigo log.
					indigo.server.log(u"\"" + device.name + u"\" start dimming", 'Sent Hue Lights')
					# Add to list.
					self.dimmingList.append(device.id)

		return

	# Set Brightness
	########################################
	def setBrightness(self, action, device):
		self.debugLog(u"setBrightness: device: " + device.name + u", action:\n" + str(action))

		brightnessSource = action.props.get('brightnessSource', False)
		brightness = action.props.get('brightness', False)
		brightnessVarId = action.props.get('brightnessVariable', False)
		brightnessDevId = action.props.get('brightnessDevice', False)
		useRateVariable = action.props.get('useRateVariable', False)
		rate = action.props.get('rate', False)
		rateVarId = action.props.get('rateVariable', False)

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Validate the action properties.
		if not brightnessSource:
			# The dimmer level source wasn't specified. Try to figure out
			#   the intended source based on passed data in the action call.
			if brightness.__class__ != bool:
				brightnessSource = "custom"
			elif brightnessVarId:
				brightnessSource = "variable"
			elif brightnessDevId:
				brightnessSource = "dimmer"
			else:
				errorText = u"No brightness source information was provided."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None

		if brightnessSource == "custom":
			if brightness == False and brightness.__class__ != int:
				errorText = u"No brightness level was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			else:
				try:
					brightness = int(brightness)
					if brightness < 0 or brightness > 100:
						errorText = u"Brightness level " + str(brightness) + u" is outside the acceptable range of 0 to 100."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
				except ValueError:
					errorText = u"Brightness level \"" + str(brightness) + u"\" is invalid. Brightness values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			self.debugLog(u"Brightness (source: custom): " + str(brightness) + u", class: " + str(brightness.__class__))

		elif brightnessSource == "variable":
			if not brightnessVarId:
				errorText = u"No variable containing the brightness level was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			else:
				try:
					brightnessVar = indigo.variables[int(brightnessVarId)]
					# Embedding float method inside int method allows for fractional
					#   data but just drops everything after the decimal.
					brightness = int(float(brightnessVar.value))
					if brightness < 0 or brightness > 100:
						errorText = u"Brightness level " + str(brightness) + u" found in variable \"" + brightnessVar.name + u"\" is outside the acceptable range of 0 to 100."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
				except ValueError:
					errorText = u"Brightness level \"" + str(brightnessVar.value) + u"\" found in variable \"" + brightnessVar.name + u"\" is invalid. Brightness values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
				except IndexError:
					errorText = u"The specified variable (ID " + str(brightnessVarId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			self.debugLog(u"Brightness (source: variable): " + str(brightness) + u", class: " + str(brightness.__class__))

		elif brightnessSource == "dimmer":
			if not brightnessDevId:
				errorText = u"No dimmer was specified as the brightness level source."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			else:
				# See if the submitted value is a device ID or a device name.
				try:
					brightnessDevId = int(brightnessDevId)
					# Value is a device ID number.
				except ValueError:
					try:
						brightnessDevId = indigo.devices[brightnessDevId].name
						# Value is a device name.
					except KeyError:
						errorText = u"No device with the name \"" + str(brightnessDevId) + u"\" could be found in the Indigo database."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
				try:
					brightnessDev = indigo.devices[brightnessDevId]
					brightness = int(brightnessDev.states.get('brightnessLevel', None))
					if brightness == None:
						# Looks like this isn't a dimmer after all.
						errorText = u"Device \"" + brightnessDev.name + u"\" does not appear to be a dimmer. Only dimmers can be used as brightness sources."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
					elif brightness < 0 or brightness > 100:
						errorText = u"Brightness level " + str(brightness) + u" of device \"" + brightnessDev.name + u"\" is outside the acceptable range of 0 to 100."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
				except ValueError:
					errorText = u"The device \"" + brightnessDev.name + u"\" does not have a brightness level. Please ensure that the device is a dimmer."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
				except KeyError:
					errorText = u"The specified device (ID " + str(brightnessDevId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			self.debugLog(u"Brightness (source: other dimmer): " + str(brightness) + u", class: " + str(brightness.__class__))

		else:
			errorText = u"Unrecognized brightness source \"" + str(brightnessSource) + u"\". Valid brightness sources are \"custom\", \"variable\", and \"dimmer\"."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return None

		if not useRateVariable:
			if not rate and rate.__class__ == bool:
				errorText = u"No ramp rate was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			else:
				try:
					rate = float(rate)
					if rate < 0 or rate > 540:
						errorText = u"Ramp rate value " + str(rate) + u" is outside the acceptible range of 0 to 540."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
				except ValueError:
					errorText = u"Ramp rate value \"" + str(rate) + u" is an invalid value. Ramp rate values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			self.debugLog(u"Rate: " + str(rate))

		else:
			if not rateVarId:
				errorText = u"No variable containing the ramp rate time was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			else:
				try:
					# Make sure rate is set to ""
					rate = ""
					rateVar = indigo.variables[int(rateVarId)]
					rate = float(rateVar.value)
					if rate < 0 or rate > 540:
						errorText = u"Ramp rate value \"" + str(rate) + u"\" found in variable \"" + rateVar.name + u"\" is outside the acceptible range of 0 to 540."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return None
				except ValueError:
					errorText = u"Ramp rate value \"" + str(rate) + u"\" found in variable \"" + rateVar.name + u"\" is an invalid value. Ramp rate values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
				except IndexError:
					errorText = u"The specified variable (ID " + str(brightnessVarId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
			self.debugLog(u"Rate: " + str(rate))

		# Save the new brightness level into the device properties.
		if brightness > 0:
			tempProps = device.pluginProps
			tempProps['savedBrightness'] = brightness
			self.updateDeviceProps(device, tempProps)

		# Send the command.
		self.doBrightness(device, int(round(brightness / 100.0 * 255.0)), rate)

	# Set RGB Level Action
	########################################
	def setRGB(self, action, device):
		self.debugLog(u"setRGB: device: " + device.name + ", action:\n" + str(action))

		red = action.props.get('red', 0)
		green = action.props.get('green', 0)
		blue = action.props.get('blue', 0)
		useRateVariable = action.props.get('useRateVariable', False)
		rampRate = action.props.get('rate', -1)
		rateVarId = action.props.get('rateVariable', False)

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		try:
			red = int(red)
		except ValueError:
			errorText = u"Red color value specified for \"" + device.name + u"\" is invalid."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		try:
			green = int(green)
		except ValueError:
			errorText = u"Green color value specified for \"" + device.name + u"\" is invalid."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		try:
			blue = int(blue)
		except ValueError:
			errorText = u"Blue color value specified for \"" + device.name + u"\" is invalid."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		if not useRateVariable:
			# Not using varible, so they've specificed a ramp rate.
			if rampRate == "" or rampRate == -1:
				# No ramp rate was specificed. Use the device's default rate, or 0.5.
				rampRate = device.pluginProps.get('rate', 0.5)
				# Devices can have an empty string for the default ramp rate.
				#   Catch this and use a default rate of 0.5 seconds if empty.
				if rampRate == "":
					rampRate = 0.5

			try:
				rampRate = float(rampRate)
				if rampRate < 0 or rampRate > 540:
					errorText = u"Ramp rate value " + str(rampRate) + u"\" is outside the acceptible range of 0 to 540."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			except ValueError:
				errorText = u"Ramp rate value \"" + str(rampRate) + u"\" is an invalid value. Ramp rate values can only contain numbers."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			self.debugLog(u"Rate: " + str(rampRate))

		else:
			# We're using a ramp rate variable.
			if not rateVarId:
				# No ramp rate variable was specified.
				errorText = u"No variable containing the ramp rate time was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
			else:
				# A ramp rate variable was specified.
				try:
					rateVar = indigo.variables[int(rateVarId)]
					rampRate = rateVar.value
					rampRate = float(rampRate)
					if rampRate < 0 or rampRate > 540:
						errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is outside the acceptible range of 0 to 540."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				except ValueError:
					errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is an invalid value. Ramp rate values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
				except IndexError:
					errorText = u"The specified variable (ID " + str(brightnessVarId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			self.debugLog(u"Rate: " + str(rampRate))

		# Determine the brightness based on the highest RGB value (to save in device props).
		brightness = red
		if blue > brightness:
			brightness = blue
		elif green > brightness:
			brightness = green

		# Save the new brightness level into the device properties.
		if brightness > 0:
			tempProps = device.pluginProps
			tempProps['savedBrightness'] = brightness
			self.updateDeviceProps(device, tempProps)

		# Send the command.
		self.doRGB(device, red, green, blue, rampRate)

	# Set HSB Action
	########################################
	def setHSB(self, action, device):
		self.debugLog(u"setHSB: device: " + device.name + u", action:\n" + str(action))

		hue = action.props.get('hue', 0)
		saturation = action.props.get('saturation', 0)
		brightnessSource = action.props.get('brightnessSource', "custom")
		brightness = action.props.get('brightness', False)
		brightnessVariable = action.props.get('brightnessVariable', False)
		brightnessDevice = action.props.get('brightnessDevice', False)
		useRateVariable = action.props.get('useRateVariable', False)
		rampRate = action.props.get('rate', -1)
		rateVarId = action.props.get('rateVariable', False)

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		try:
			hue = float(hue)
		except ValueError:
			# The float() cast above might fail if the user didn't enter a number:
			errorText = u"Set Hue, Saturation, Brightness for device \"%s\" -- invalid hue value (must range 0-360)" % (device.name,)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		try:
			saturation = int(saturation)
		except ValueError:
			# The int() cast above might fail if the user didn't enter a number:
			errorText = u"Set Hue, Saturation, Brightness for device \"%s\" -- invalid saturation value (must range 0-100)" % (device.name,)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		if brightnessSource == "custom":
			# Using an entered brightness value.
			if brightness:
				try:
					brightness = int(brightness)
				except ValueError:
					errorText = u"Invalid brightness value \"" + brightness + u"\" specified for device \"%s\". Value must be in the range 0-100." % (device.name)
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return

				# Make sure the brightness specified in the variable is sane.
				if brightness < 0 or brightness > 100:
					errorText = u"Brightness value \"" + str(brightness) + u"\" for device \"%s\" is outside the acceptible range of 0 to 100." % (device.name)
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			else:
				brightness = device.states['brightnessLevel']
		elif brightnessSource == "variable":
			if brightnessVariable:
				# Action properties are passed as strings. Variable and device IDs are integers
				# so we need to convert the variable ID passed in brightnessVariable to an integer.
				brightnessVariable = int(brightnessVariable)
				try:
					brightness = int(indigo.variables[brightnessVariable].value)
				except ValueError:
					errorText = u"Brightness value \"" + indigo.variables[brightnessVariable].value + u"\" specified in variable \"" + indigo.variables[brightnessVariable].name + u"\" for device \"%s\" is invalid." % (device.name)
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
				except IndexError:
					errorText = u"The brightness source variable (ID " + str(brightnessVariable) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return

				# Make sure the brightness specified in the variable is sane.
				if brightness < 0 or brightness > 100:
					errorText = u"Brightness value \"" + str(brightness) + u"\" specified in variable \"" + indigo.variables[brightnessVariable].name + u"\" is outside the acceptible range of 0 to 100."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			else:
				brightness = device.states['brightnessLevel']
		elif brightnessSource == "dimmer":
			if brightnessDevice:
				# Action properties are passed as strings. Variable and device IDs are integers
				# so we need to convert the device ID passed in brightnessDevice to an integer.
				brightnessDevice = int(brightnessDevice)
				try:
					brightness = int(indigo.devices[brightnessDevice].states['brightnessLevel'])
				except ValueError:
					errorText = u"The brightness \"" + indigo.devices[brightnessDevice].states['brightnessLevel'] + u"\" of the selected source device \"" + indigo.devices[brightnessDevice].name + u"\" is invalid."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
				except IndexError:
					errorText = u"The brightness source device (ID " + str(brightnessDevice) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			else:
				brightness = device.states['brightnessLevel']

		if not useRateVariable:
			# Not using varible, so they've specificed a ramp rate.
			if rampRate == "" or rampRate == -1:
				# No ramp rate was specificed. Use the device's default rate, or 0.5.
				rampRate = device.pluginProps.get('rate', 0.5)
				# Devices can have an empty string for the default ramp rate.
				#   Catch this and use a default rate of 0.5 seconds if empty.
				if rampRate == "":
					rampRate = 0.5

			try:
				rampRate = float(rampRate)
				if rampRate < 0 or rampRate > 540:
					errorText = u"Ramp rate value " + str(rampRate) + u"\" is outside the acceptible range of 0 to 540."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			except ValueError:
				errorText = u"Ramp rate value \"" + str(rampRate) + u"\" is an invalid value. Ramp rate values can only contain numbers."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			self.debugLog(u"Rate: " + str(rampRate))

		else:
			# We're using a ramp rate variable.
			if not rateVarId:
				# No ramp rate variable was specified.
				errorText = u"No variable containing the ramp rate time was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
			else:
				# A ramp rate variable was specified.
				try:
					rateVar = indigo.variables[int(rateVarId)]
					rampRate = rateVar.value
					rampRate = float(rampRate)
					if rampRate < 0 or rampRate > 540:
						errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is outside the acceptible range of 0 to 540."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				except ValueError:
					errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is an invalid value. Ramp rate values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
				except IndexError:
					errorText = u"The specified variable (ID " + str(brightnessVarId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			self.debugLog(u"Rate: " + str(rampRate))

		# Scale these values to match Hue
		brightness = int(ceil(brightness / 100.0 * 255.0))
		saturation = int(ceil(saturation / 100.0 * 255.0))
		hue = int(round(hue * 182.0))

		# Save the new brightness level into the device properties.
		if brightness > 0:
			tempProps = device.pluginProps
			tempProps['savedBrightness'] = brightness
			self.updateDeviceProps(device, tempProps)

		# Send the command.
		self.doHSB(device, hue, saturation, brightness, rampRate)

	# Set xyY Action
	########################################
	def setXYY(self, action, device):
		self.debugLog(u"setXYY calld. device: " + device.name + u", action:\n" + str(action))

		colorX = action.props.get('xyy_x', 0)
		colorY = action.props.get('xyy_y', 0)
		brightness = action.props.get('xyy_Y', 0)
		useRateVariable = action.props.get('useRateVariable', False)
		rampRate = action.props.get('rate', -1)
		rateVarId = action.props.get('rateVariable', False)

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		try:
			colorX = float(colorX)
		except ValueError:
			# The float() cast above might fail if the user didn't enter a number:
			errorText = u"Set chromatisety x, y, and Y values for the device \"%s\" -- invalid x value (must be in the range of 0.0-1.0)" % (device.name,)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		try:
			colorY = float(colorY)
		except ValueError:
			# The float() cast above might fail if the user didn't enter a number:
			errorText = u"Set chromatisety x, y, and Y values for the device \"%s\" -- invalid y value (must be in the range of 0.0-1.0)" % (device.name,)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		try:
			brightness = float(brightness)
		except ValueError:
			# The float() cast above might fail if the user didn't enter a number:
			errorText = u"Set chromatisety x, y, and Y values for the device \"" + device.name + u"\" -- invalid Y value of \"" + str(brightness) + u"\" (must be in the range of 0.0-1.0)"
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		if not useRateVariable:
			# Not using varible, so they've specificed a ramp rate.
			if rampRate == "" or rampRate == -1:
				# No ramp rate was specificed. Use the device's default rate, or 0.5.
				rampRate = device.pluginProps.get('rate', 0.5)
				# Devices can have an empty string for the default ramp rate.
				#   Catch this and use a default rate of 0.5 seconds if empty.
				if rampRate == "":
					rampRate = 0.5

			try:
				rampRate = float(rampRate)
				if rampRate < 0 or rampRate > 540:
					errorText = u"Ramp rate value " + str(rampRate) + u"\" is outside the acceptible range of 0 to 540."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			except ValueError:
				errorText = u"Ramp rate value \"" + str(rampRate) + u"\" is an invalid value. Ramp rate values can only contain numbers."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			self.debugLog(u"Rate: " + str(rampRate))

		else:
			# We're using a ramp rate variable.
			if not rateVarId:
				# No ramp rate variable was specified.
				errorText = u"No variable containing the ramp rate time was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
			else:
				# A ramp rate variable was specified.
				try:
					rateVar = indigo.variables[int(rateVarId)]
					rampRate = rateVar.value
					rampRate = float(rampRate)
					if rampRate < 0 or rampRate > 540:
						errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is outside the acceptible range of 0 to 540."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				except ValueError:
					errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is an invalid value. Ramp rate values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
				except IndexError:
					errorText = u"The specified variable (ID " + str(brightnessVarId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			self.debugLog(u"Rate: " + str(rampRate))

		# Scale the brightness values to match Hue system requirements.
		brightness = int(ceil(brightness * 255.0))

		# Save the new brightness level into the device properties.
		if brightness > 0:
			tempProps = device.pluginProps
			tempProps['savedBrightness'] = brightness
			self.updateDeviceProps(device, tempProps)

		# Send the command.
		self.doXYY(device, colorX, colorY, brightness, rampRate)

	# Set Color Temperature Action
	########################################
	def setColorTemperature(self, action, device):
		self.debugLog(u"setColorTemperature: device: " + device.name + ", action:\n" + str(action))

		bulbId = device.pluginProps.get('bulbId', None)
		groupId = device.pluginProps.get('groupId', None)

		# Get the Hue "color recipe" selection. Use "custom" if not specified.
		#   (The use of the property name "preset" pre-dates the implementation
		#   of the Save and Recall Preset functions within the plugin.  The
		#   term "preset" was originally used in the Hue app distributed by
		#   Phillips, who've since decided to call them "recipes."  Now it's
		#   just confusing).
		preset = action.props.get('preset', "custom")
		temperatureSource = action.props.get('temperatureSource', "custom")
		temperature = action.props.get('temperature', 2800)
		temperatureVariable = action.props.get('temperatureVariable', False)
		brightnessSource = action.props.get('brightnessSource', "custom")
		brightness = action.props.get('brightness', False)
		brightnessVariable = action.props.get('brightnessVariable', False)
		brightnessDevice = action.props.get('brightnessDevice', False)
		useRateVariable = action.props.get('useRateVariable', False)
		rampRate = action.props.get('rate', -1)
		rateVarId = action.props.get('rateVariable', False)

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		if preset == "custom":
			# Using a custom color recipe (temperature/brightness combination).
			if temperatureSource == "custom":
				try:
					temperature = int(temperature)
				except ValueError:
					# The int() cast above might fail if the user didn't enter a number:
					errorText = u"Invalid color temperature specified for device \"%s\".  Value must be in the range 2000 to 6500." % (device.name)
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			elif temperatureSource == "variable":
				if temperatureVariable:
					# Action properties are passed as strings. Variable and device IDs are integers
					# so we need to convert the variable ID passed in brightnessVariable to an integer.
					temperatureVariable = int(temperatureVariable)
					try:
						temperature = int(indigo.variables[temperatureVariable].value)
					except ValueError:
						errorText = u"Invalid color temperature value \"" + indigo.variables[temperatureVariable].value + u"\" found in source variable \"" + indigo.variables[temperatureVariable].name + u"\" for device \"%s\"." % (device.name)
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return

					# Make sure the color temperature specified in the variable is sane.
					if temperature < 2000 or temperature > 6500:
						errorText = u"Color temperature value \"" + str(temperature) + u"\" found in source variable \"" + indigo.variables[temperatureVariable].name + u"\" for device \"%s\" is outside the acceptible range of 2000 to 6500." % (device.name)
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				else:
					temperature = device.states['colorTemp']

			if brightnessSource == "custom":
				# Using an entered brightness value.
				if brightness:
					try:
						brightness = int(brightness)
					except ValueError:
						errorText = u"Invalid brightness value \"" + brightness + u"\" specified for device \"%s\". Value must be in the range 0-100." % (device.name)
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return

					# Make sure the brightness specified in the variable is sane.
					if brightness < 0 or brightness > 100:
						errorText = u"Brightness value \"" + str(brightness) + u"\" for device \"%s\" is outside the acceptible range of 0 to 100." % (device.name)
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				else:
					brightness = device.states['brightnessLevel']
			elif brightnessSource == "variable":
				if brightnessVariable:
					# Action properties are passed as strings. Variable and device IDs are integers
					# so we need to convert the variable ID passed in brightnessVariable to an integer.
					brightnessVariable = int(brightnessVariable)
					try:
						brightness = int(indigo.variables[brightnessVariable].value)
					except ValueError:
						errorText = u"Brightness value \"" + indigo.variables[brightnessVariable].value + u"\" specified in variable \"" + indigo.variables[brightnessVariable].name + u"\" for device \"%s\" is invalid." % (device.name)
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
					except IndexError:
						errorText = u"The brightness source variable (ID " + str(brightnessVariable) + u") does not exist in the Indigo database."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return

					# Make sure the brightness specified in the variable is sane.
					if brightness < 0 or brightness > 100:
						errorText = u"Brightness value \"" + str(brightness) + u"\" specified in variable \"" + indigo.variables[brightnessVariable].name + u"\" is outside the acceptible range of 0 to 100."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				else:
					brightness = device.states['brightnessLevel']
			elif brightnessSource == "dimmer":
				if brightnessDevice:
					# Action properties are passed as strings. Variable and device IDs are integers
					# so we need to convert the device ID passed in brightnessDevice to an integer.
					brightnessDevice = int(brightnessDevice)
					try:
						brightness = int(indigo.devices[brightnessDevice].states['brightnessLevel'])
					except ValueError:
						errorText = u"The brightness \"" + indigo.devices[brightnessDevice].states['brightnessLevel'] + u"\" of the selected source device \"" + indigo.devices[brightnessDevice].name + u"\" is invalid."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
					except IndexError:
						errorText = u"The brightness source device (ID " + str(brightnessDevice) + u") does not exist in the Indigo database."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				else:
					brightness = device.states['brightnessLevel']

			# Scale the brightness value for use with Hue.
			brightness = int(round(brightness / 100.0 * 255.0))

		if not useRateVariable:
			# Not using varible, so they've specificed a ramp rate.
			if rampRate == "" or rampRate == -1:
				# No ramp rate was specificed. Use the device's default rate, or 0.5.
				rampRate = device.pluginProps.get('rate', 0.5)
				# Devices can have an empty string for the default ramp rate.
				#   Catch this and use a default rate of 0.5 seconds if empty.
				if rampRate == "":
					rampRate = 0.5

			try:
				rampRate = float(rampRate)
				if rampRate < 0 or rampRate > 540:
					errorText = u"Ramp rate value " + str(rampRate) + u"\" is outside the acceptible range of 0 to 540."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return None
			except ValueError:
				errorText = u"Ramp rate value \"" + str(rampRate) + u"\" is an invalid value. Ramp rate values can only contain numbers."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return None
			self.debugLog(u"Rate: " + str(rampRate))

		else:
			# We're using a ramp rate variable.
			if not rateVarId:
				# No ramp rate variable was specified.
				errorText = u"No variable containing the ramp rate time was specified."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
			else:
				# A ramp rate variable was specified.
				try:
					rateVar = indigo.variables[int(rateVarId)]
					rampRate = rateVar.value
					rampRate = float(rampRate)
					if rampRate < 0 or rampRate > 540:
						errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is outside the acceptible range of 0 to 540."
						self.errorLog(errorText)
						# Remember the error.
						self.lastErrorMessage = errorText
						return
				except ValueError:
					errorText = u"Ramp rate value \"" + str(rampRate) + u"\" found in variable \"" + rateVar.name + u"\" is an invalid value. Ramp rate values can only contain numbers."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
				except IndexError:
					errorText = u"The specified variable (ID " + str(brightnessVarId) + u") does not exist in the Indigo database."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					return
			self.debugLog(u"Rate: " + str(rampRate))

		# Configure presets
		if preset == "concentrate":
			brightness = 219
			temperature = 4292
		elif preset == "relax":
			brightness = 144
			temperature = 2132
		elif preset == "energize":
			brightness = 203
			temperature = 6410
		elif preset == "reading":
			brightness = 240
			temperature = 2890

		# Save the new brightness level into the device properties.
		if brightness > 0:
			tempProps = device.pluginProps
			tempProps['savedBrightness'] = brightness
			self.updateDeviceProps(device, tempProps)

		# Send the command.
		self.doColorTemperature(device, temperature, brightness, rampRate)

	# Set Single Alert Action
	########################################
	def alertOnce(self, action, device):
		self.debugLog(u"alertOnce: device: " + device.name + u", action:\n" + str(action))

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		self.doAlert(device, "select")

	# Set Long Alert Action
	########################################
	def longAlert(self, action, device):
		self.debugLog(u"longAlert: device: " + device.name + u", action:\n" + str(action))

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		self.doAlert(device, "lselect")

	# Stop Alert Action
	########################################
	def stopAlert(self, action, device):
		self.debugLog(u"stopAlert: device: " + device.name + u", action:\n" + str(action))

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		self.doAlert(device, "none")

	# Set Effect Action
	########################################
	def effect(self, action, device):
		self.debugLog(u"effect: device: " + device.name + u", action:\n" + str(action))

		# Act based on device type.
		if device.deviceTypeId == "hueGroup":
			# Sanity check on group ID
			groupId = device.pluginProps.get('groupId', None)
			if groupId is None or groupId == 0:
				errorText = u"No group ID selected for device \"%s\". Check settings for this device and select a Hue Group to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return
		else:
			# Sanity check on bulb ID
			bulbId = device.pluginProps.get('bulbId', None)
			if bulbId is None or bulbId == 0:
				errorText = u"No bulb ID selected for device \"%s\". Check settings for this device and select a Hue Device to control." % (device.name)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		effect = action.props.get('effect', False)
		if not effect:
			errorText = u"No effect specified."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return False
		else:
			self.doEffect(device, effect)

	# Save Preset Action
	########################################
	def savePreset(self, action, device):
		self.debugLog(u"savePreset called. action values:\n" + str(action) + u"\nDevice/Type ID:\n" + str(device) + "\n")
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = u""
		actionType = "action"
		# Work with both Menu and Action actions.
		try:
			device = indigo.devices[int(action.get('deviceId', 0))]
			actionType = "menu"
		except AttributeError:
			# This is an action, not a menu call.
			pass

		# Sanity check on bulb ID
		bulbId = device.pluginProps.get('bulbId', None)
		if bulbId is None or bulbId == 0:
			errorText = u"No Hue device ID selected for \"%s\". Check settings and select a Hue device to control." % (device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the presetId.
		if actionType == "menu":
			presetId = action.get('presetId', False)
		else:
			presetId = action.props.get('presetId', False)

		if not presetId:
			errorText = u"No Preset specified."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return False
		else:
			# Convert to integer.
			presetId = int(presetId)
			# Subtract 1 because key values are 0-based.
			presetId -= 1

		# Get the Ramp Rate.
		if actionType == "menu":
			rampRate = action.get('rate', "")
			# Validate Ramp Rate.
			if len(rampRate) > 0:
				try:
					rampRate = float(rampRate)
					if (rampRate < 0) or (rampRate > 540):
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate']
						return (False, action, errorsDict)
				except ValueError:
					errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate']
					return (False, action, errorsDict)
				except Exception, e:
					errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate']
					return (False, action, errorsDict)
		else:
			rampRate = action.props.get('rate', "")

		# If there was no Ramp Rate specified, use -1.
		if rampRate == "":
			rampRate = -1

		# Get the plugin prefs and populate them into a local array.
		presets = list()
		for num in range(0,len(self.pluginPrefs['presets'])):
			tempPresetName = self.pluginPrefs['presets'][num][0]
			tempPresetData = self.pluginPrefs['presets'][num][1]
			try:
				# Prior to version 1.2.4, the Ramp Rate index did not exist.
				tempPresetRate = self.pluginPrefs['presets'][num][2]
			except IndexError:
				tempPresetRate = -1
			presets.append(list((tempPresetName, tempPresetData, tempPresetRate)))

		# Update the new array with the submitted values.
		if actionType == "menu":
			presetName = action.get('presetName', False)
			# Return an error if the presetName is too long.
			if len(presetName) > 50:
				errorsDict['presetName'] = u"The Preset Name is too long. Please choose a name that is 50 or fewer characters long."
				errorsDict['showAlertText'] += errorsDict['presetName']
				return (False, action, errorsDict)

		else:
			presetName = action.props.get('presetName', False)

		if not presetName:
			presetName = ""

		# If the submitted name is not blank, change the name in the prefs.
		if presetName != "":
			# (Index 0 = preset name).
			presets[presetId][0] = presetName
		else:
			# Submitted presetName is blank. Use the current presetName for logging.
			presetName = presets[presetId][0]

		# Create the states list dict.
		for key, value in device.states.iteritems():
			# (Index 1 = preset data).
			presets[presetId][1][key] = value

		# Add the Ramp Rate to the Preset.
		if rampRate != -1:	# May still be a sring if passed by embedded script call.
			try:
				rampRate = float(rampRate)
				if (rampRate < 0) or (rampRate > 540):
					errorText = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds. Value \"" + str(rampRate) + u"\" ignored."
					self.errorLog(errorText)
					# Remember the error.
					self.lastErrorMessage = errorText
					rampRate = -1
			except ValueError:
				errorText = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds. Value \"" + str(rampRate) + u"\" ignored."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = -1
			except Exception, e:
				errorText = u"Invalid Ramp Rate value \"" + str(rampRate) + u"\". Error was: " + str(e)
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				rampRate = -1
		else:
			# No Ramp Rate submitted. Use -1 to indicate this.
			rampRate = -1
		# (Index 2 = ramp rate).
		presets[presetId][2] = rampRate

		# Save the device's states to the preset.
		self.pluginPrefs['presets'] = presets

		# Log the action.
		if rampRate == -1:
			indigo.server.log(u"\"" + device.name + u"\" states saved to Preset " + str(presetId + 1) + u" (" + presetName + u")")
		else:
			indigo.server.log(u"\"" + device.name + u"\" states saved to Preset " + str(presetId + 1) + u" (" + presetName + u") with ramp rate " + str(rampRate) + u" sec.")

		# Return a tuple if this is a menu item action.
		if actionType == "menu":
			return (True, action)

	# Recall Preset Action
	########################################
	def recallPreset(self, action, device):
		self.debugLog(u"recallPreset called. action values:\n" + str(action) + u"\nDevice/Type ID:\n" + str(device) + u"\n")
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = u""
		actionType = "action"
		# Work with both Menu and Action actions.
		try:
			device = indigo.devices[int(action.get('deviceId', 0))]
			actionType = "menu"
		except AttributeError:
			# This is an action, not a menu call.
			pass

		# Sanity check on bulb ID
		bulbId = device.pluginProps.get('bulbId', None)
		if bulbId is None or bulbId == 0:
			errorText = u"No Hue device ID selected for \"%s\". Check settings and select a Hue device to control." % (device.name)
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the presetId.
		if actionType == "menu":
			presetId = action.get('presetId', False)
		else:
			presetId = action.props.get('presetId', False)

		if not presetId:
			errorText = u"No Preset specified."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return False
		else:
			# Convert to integer.
			presetId = int(presetId)
			# Subtract 1 because key values are 0-based.
			presetId -= 1

		# Get the Ramp Rate.
		if actionType == "menu":
			rampRate = action.get('rate', "")
			# Validate Ramp Rate.
			if len(rampRate) > 0:
				try:
					rampRate = float(rampRate)
					# Round the number to the nearest 10th.
					rampRate = round(rampRate, 1)
					if (rampRate < 0) or (rampRate > 540):
						errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
						errorsDict['showAlertText'] += errorsDict['rate']
						return (False, action, errorsDict)
				except ValueError:
					errorsDict['rate'] = u"Ramp Rate must be a number between 0 and 540 seconds and can be in increments of 0.1 seconds."
					errorsDict['showAlertText'] += errorsDict['rate']
					return (False, action, errorsDict)
				except Exception, e:
					errorsDict['rate'] = u"Invalid Ramp Rate value: " + str(e)
					errorsDict['showAlertText'] += errorsDict['rate']
					return (False, action, errorsDict)
		else:
			rampRate = action.props.get('rate', "")

		# If there is no Ramp Rate specified, use -1.
		if rampRate == "":
			rampRate = -1

		# Get the modelId from the device.
		modelId = device.pluginProps.get('modelId', False)
		if not modelId:
			errorText = u"The \"" + device.name + u"\" devuce is not a Hue device. Please select a Hue device for this action."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		elif modelId not in kCompatibleDeviceIDs:
			errorText = u"The \"" + device.name + u"\" device is not a compatible Hue device. Please select a compatible Hue device."
			self.errorLog(errorText)
			# Remember the error.
			self.lastErrorMessage = errorText
			return

		# Get the data from the preset in the plugin prefs.
		presetName = self.pluginPrefs['presets'][presetId][0]
		presetData = self.pluginPrefs['presets'][presetId][1]
		try:
			# Prior to version 1.2.4, this key did not exist in the presets.
			presetRate = self.pluginPrefs['presets'][presetId][2]
			# Round the saved preset ramp rate to the nearest 10th.
			presetRate = round(presetRate, 1)
		except Exception, e:
			# Key probably doesn't exist. Proceed as if no rate was saved.
			presetRate = -1
			pass

		# If there was no Ramp Rate override specified in the recall action,
		#   use the one saved in the Preset (if any).
		if rampRate == -1:
			rampRate = presetRate

		# If the presetData has no data, return an error as this Preset is empty.
		if len(presetData) < 1:
			# Return an error if the Preset is empty (since there's nothing to display).
			if actionType == "menu":
				errorsDict['presetId'] = u"This Preset is empty. Please select a Preset that contains data (the number will have an asterisk (*) next to it)."
				errorsDict['showAlertText'] += errorsDict['presetId']
				return (False, action, errorsDict)
			else:
				errorText = u"Preset " + str(presetId + 1) + u" (" + presetName + u") is empty. The \"" + device.name + u"\" device was not chnaged."
				self.errorLog(errorText)
				# Remember the error.
				self.lastErrorMessage = errorText
				return

		# Determine whether the target device supports color.
		supportsColor = True
		if modelId in kLivingWhitesDeviceIDs:
			supportsColor = False

		# Determine whether the target device supports color temperature.
		supportsColorTemperature = False
		if modelId in kHueBulbDeviceIDs:
			supportsColorTemperature = True

		# Get the brightness level (which is common to all devices).
		brightnessLevel = presetData.get('brightnessLevel', 100)
		# Convert the brightnessLevel to 0-255 range for use in the light
		#   changing method calls.
		brightness = int(round(brightnessLevel / 100.0 * 255.0))

		# Act based on the capabilities of the target device.
		if supportsColor:
			if supportsColorTemperature:
				# This device supports all currently known color modes.
				#   Now determine which mode was saved in the preset and use
				#   use it with the target device (use "ct" as the default).
				colorMode = presetData.get('colorMode', "ct")

				if colorMode == "ct":
					# Get the color temperature state (use 2800 as default).
					colorTemp = presetData.get('colorTemp', 2800)

					# Make the change to the light.
					self.doColorTemperature(device, colorTemp, brightness, rampRate)

				elif colorMode == "hs":
					# Get the hue (use 0 as the default).
					hue = presetData.get('hue', 0)
					# Conver the hue from 0-360 range to 0-65535 range.
					hue = int(round(hue * 182.0))
					# Get the saturation (use 100 as the default).
					saturation = presetData.get('saturation', 100)
					# Convert from 0-100 range to 0-255 range.
					saturation = int(round(saturation / 100.0 * 255.0))

					# Make the light change.
					self.doHSB(device, hue, saturation, brightness, rampRate)

				elif colorMode == "xy":
					# Get the x and y values (using 0.35 as default for both).
					colorX = presetData.get('colorX', 0.35)
					colorY = presetData.get('colorY', 0.35)

					# Make the light change.
					self.doXYY(device, colorX, colorY, brightness, rampRate)

			else:
				# This device supports color, but not color temperature.
				#   Now determine which mode was saved in the preset and use
				#   use it with the target device (use "hs" as the default).
				colorMode = presetData.get('colorMode', "hs")

				if colorMode == "ct":
					# The target device doesn't suppor color temperature.
					#   Use an alternate color rendering method such as HSB.
					colorMode = "xy"

				if colorMode == "hs":
					# Get the hue (use 0 as the default).
					hue = presetData.get('hue', 0)
					# Conver the hue from 0-360 range to 0-65535 range.
					hue = int(round(hue * 182.0))
					# Get the saturation (use 100 as the default).
					saturation = presetData.get('saturation', 100)
					# Convert from 0-100 range to 0-255 range.
					saturation = int(round(saturation / 100.0 * 255.0))

					# Make the light change.
					self.doHSB(device, hue, saturation, brightness, rampRate)

				elif colorMode == "xy":
					# Get the x and y values (using 0.35 as default for both).
					colorX = presetData.get('colorX', 0.35)
					colorY = presetData.get('colorY', 0.35)

					# Make the light change.
					self.doXYY(device, colorX, colorY, brightness, rampRate)

		else:
			# This device doesn't support color.  Just set the brightness.
			self.doBrightness(device, brightness, rampRate)

		# Log the action.
		if rampRate == -1:
			indigo.server.log(u"\"" + device.name + u"\" states set to Preset " + str(presetId + 1) + u" (" + presetName + u")")
		else:
			indigo.server.log(u"\"" + device.name + u"\" states set to Preset " + str(presetId + 1) + u" (" + presetName + u") at ramp rate " + str(rampRate) + u" sec.")

		# Return a tuple if this is a menu item action.
		if actionType == "menu":
			return (True, action)

	# Display Preset Menu Action
	########################################
	def displayPreset(self, valuesDict, typeId):
		self.debugLog(u"displayPreset called. action values:\n" + str(valuesDict) + u"\nType ID:\n" + str(typeId) + "\n")
		errorsDict = indigo.Dict()
		errorsDict['showAlertText'] = u""

		# Get the presetId.
		presetId = valuesDict.get('presetId', False)

		if not presetId:
			errorsDict['presetId'] = u"No Preset is selected."
			errorsDict['showAlertText'] += errorsDict['presetId']
			return (False, valuesDict, errorsDict)

		else:
			# Convert to integer.
			presetId = int(presetId)
			# Subtract 1 because key values are 0-based.
			presetId -= 1

		# Get the data from the preset in the plugin prefs.
		presetName = self.pluginPrefs['presets'][presetId][0]
		presetData = self.pluginPrefs['presets'][presetId][1]
		try:
			# Prior to version 1.2.4, this key did not exist in the presets.
			presetRate = self.pluginPrefs['presets'][presetId][2]
			# Round the saved preset ramp rate to the nearest 10th.
			presetRate = round(presetRate, 1)
		except Exception, e:
			# Key probably doesn't exist. Proceed as if no rate was saved.
			presetRate = -1
			pass

		# Return an error if the Preset is empty (since there's nothing to display).
		if len(presetData) < 1:
			errorsDict['presetId'] = u"This Preset is empty. Please select a Preset that contains data (the number will have an asterisk (*) next to it)."
			errorsDict['showAlertText'] += errorsDict['presetId']
			return (False, valuesDict, errorsDict)

		# Display the Preset data in the Indigo log.
		logRampRate = str(presetRate) + u" sec."
		if presetRate == -1:
			logRampRate = u"(none specified)"
		indigo.server.log(u"Displaying Preset " + str(presetId + 1) + u" (" + presetName + u") stored data:\nRamp Rate: " + logRampRate + u"\n" + str(presetData))

		# Return a tuple to dismiss the menu item dialog.
		return (True, valuesDict)

	# Toggle Debug Logging Menu Action
	########################################
	def toggleDebugging(self):
		if self.debug:
			indigo.server.log("Turning off debug logging")
			self.pluginPrefs['showDebugInfo'] = False
		else:
			indigo.server.log("Turning on debug logging")
			self.pluginPrefs['showDebugInfo'] = True
		self.debug = not self.debug

	# Reload hub configuration menu action
	########################################
	def updateAllHueListsFromMenu(self, valuesDict, typeId):
		hubId = valuesDict.get("hubId", None)
		if hubId is None or hubId == "":
			return (False, valuesDict)
		hubDevice = indigo.devices[int(hubId)]
		self.updateAllHueLists(hubDevice)
		return (True, valuesDict)
