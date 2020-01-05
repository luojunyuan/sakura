# coding: utf8
# sktr.py
# 10/8/2012 jichi

__all__ = 'tr_', 'notr_', 'utr_'

from PySide2.QtCore import QObject
from .skclass import memoized

#import os
#LOCATION = os.path.dirname(__file__) + '/tr'
#TRANSLATIONS = frozenset(('ja_JP', 'zh_TW', 'zh_CN'))

# The class name must be same as sakurakit.js


class sakurakit(QObject):
    """这里没有输出?\n哪里有sakurakit.js\n
    依赖项：PySide2 skclass"""
    # Dummy translations to fool pyside-lupdate

    def translations(self):
        return (
            # Terms
            self.tr("Javascript"),
            self.tr("Python"),
            self.tr("BBCode"),

            # Countries

            self.tr("Mainland China"),

            # Languages
            self.tr("English"),
            self.tr("Japanese"),
            self.tr("Chinese"),
            self.tr("Korean"),
            self.tr("Hangul"),

            self.tr("German"),
            self.tr("French"),
            self.tr("Italian"),
            self.tr("Spanish"),
            self.tr("Portuguese"),
            self.tr("Russian"),
            self.tr("Polish"),
            self.tr("Dutch"),

            self.tr("Thai"),
            self.tr("Vietnamese"),
            self.tr("Malaysian"),
            self.tr("Indonesian"),
            self.tr("Arabic"),
            self.tr("Hebrew"),

            self.tr("Tagalog"),
            self.tr("Filipino"),

            self.tr("Czech"),
            self.tr("Belarusian"),
            self.tr("Bulgarian"),
            self.tr("Danish"),
            self.tr("Estonian"),
            self.tr("Finnish"),
            self.tr("Greek"),
            self.tr("Hungarian"),
            self.tr("Norwegian"),
            self.tr("Latvian"),
            self.tr("Lithuanian"),
            self.tr("Romanian"),
            self.tr("Slovak"),
            self.tr("Slovenian"),
            self.tr("Swedish"),
            self.tr("Ukrainian"),
            self.tr("Turkish"),

            self.tr("Latin"),
            self.tr("Cyrillic"),

            self.tr("Traditional Chinese"),
            self.tr("Simplified Chinese"),

            self.tr("ja"),
            self.tr("en"),
            self.tr("zh"),
            self.tr("zht"),
            self.tr("zhs"),
            self.tr("ko"),
            self.tr("th"),
            self.tr("vi"),
            self.tr("id"),
            self.tr("tl"),
            self.tr("et"),
            self.tr("lt"),
            self.tr("lv"),
            self.tr("ms"),
            self.tr("he"),
            self.tr("ar"),
            self.tr("cs"),
            self.tr("be"),
            self.tr("bg"),
            self.tr("da"),
            self.tr("de"),
            self.tr("el"),
            self.tr("fi"),
            self.tr("fr"),
            self.tr("hu"),
            self.tr("it"),
            self.tr("es"),
            # self.tr("no"),
            self.tr("nb"),
            self.tr("nl"),
            self.tr("pl"),
            self.tr("pt"),
            self.tr("ro"),
            self.tr("ru"),
            self.tr("sk"),
            self.tr("sl"),
            self.tr("sv"),
            self.tr("tr"),
            self.tr("uk"),

            self.tr("he"),  # Hebrew

            # Actions
            self.tr("Show {0}"),
            self.tr("Hide {0}"),

            self.tr("Scroll to Top"), self.tr("Scroll to top"),
            self.tr("Scroll to Bottom"), self.tr("Scroll to bottom"),

            self.tr("Restore default settings"),

            self.tr("Click"), self.tr("click"),
            self.tr("Double Click"), self.tr(
                "Double click"), self.tr("double click"),
            self.tr("Double-click"), self.tr("double-click"),
            self.tr("Left Click"), self.tr("Left click"),
            self.tr("Left-Click"), self.tr("Left-click"),
            self.tr("Middle Click"), self.tr("Middle click"),
            self.tr("Middle-Click"), self.tr("Middle-click"),
            self.tr("Right Click"), self.tr("Right click"),
            self.tr("Right-Click"), self.tr("Right-click"),

            self.tr("Space"),

            self.tr("About"),
            self.tr("About {0}"),
            self.tr("Add"),
            self.tr("Advanced"),
            self.tr("Append"),
            self.tr("Back"),
            self.tr("Browse"),
            self.tr("Buy"),
            self.tr("Cancel"),
            self.tr("Category"),
            self.tr("Chat"), self.tr("chat"),
            self.tr("Check"),
            self.tr("Clear"),
            self.tr("Close"),
            self.tr("Cluster"),
            self.tr("Confirm"),
            self.tr("Copy"),
            self.tr("Copy All"),
            self.tr("Create"), self.tr("Creation"),
            self.tr("Cut"),
            self.tr("Delete"), self.tr("delete"),
            self.tr("Del"), self.tr("del"),
            self.tr("Disable"), self.tr("disable"),
            self.tr("Disabled"), self.tr("disabled"),
            self.tr("Download"), self.tr("download"),
            self.tr("Downloads"),
            self.tr("Downloading"),
            self.tr("Duplicate"),
            self.tr("Edit"), self.tr("edit"),
            self.tr("Empty"), self.tr("empty"),
            self.tr("Enter"),
            self.tr("Enable"), self.tr("enable"),
            self.tr("Enabled"), self.tr("enabled"),
            self.tr("Equal"), self.tr("equal"),
            self.tr("Escape"),
            self.tr("Export"),
            self.tr("Extra"), self.tr("extra"),
            self.tr("Filter"),
            self.tr("Forward"),
            self.tr("Full screen"),
            self.tr("Finish"),
            self.tr("Hide"), self.tr("hide"),
            self.tr("Improve"), self.tr("improve"),
            self.tr("Ignore"), self.tr("ignore"),
            self.tr("Ignored"), self.tr("ignored"),
            self.tr("Install"),
            self.tr("Launch"),
            self.tr("Link"),
            self.tr("Links"),
            self.tr("Load"), self.tr("load"),
            self.tr("Lock"), self.tr("lock"),
            self.tr("Locked"), self.tr("locked"),
            self.tr("Lookup"),
            self.tr("Move"),
            self.tr("Next"),
            self.tr("None"), self.tr("none"),
            self.tr("Note"),
            self.tr("OK"),
            self.tr("Open"),
            self.tr("Opening"),
            self.tr("Other"), self.tr("other"),
            self.tr("Overwrite"),
            self.tr("Paste"),
            self.tr("Play"),
            self.tr("Pause"),
            self.tr("Permission"), self.tr("Permissions"),
            self.tr("Pop-up"), self.tr("pop-up"),
            self.tr("Popup"),
            self.tr("Previous"),
            self.tr("Read"),
            self.tr("Recommend"), self.tr("recommend"),
            self.tr("Recommended"), self.tr("recommended"),
            self.tr("Refresh"),
            self.tr("Recent Changes"), self.tr("Recent changes"),
            self.tr("Register"),
            self.tr("Remove"),
            self.tr("Replicate"),
            self.tr("Reset"), self.tr("reset"),
            self.tr("Resize"),
            self.tr("Restart"),
            self.tr("Resume"),
            self.tr("Reply"),
            self.tr("Save"), self.tr("save"),
            self.tr("Secondary"), self.tr("secondary"),
            self.tr("Select"),
            self.tr("Select Word"),
            self.tr("Select All"),
            self.tr("Search"),
            self.tr("Searching"),
            self.tr("Show"), self.tr("show"),
            self.tr("Software Update"),
            self.tr("Source"),
            self.tr("Speed"),
            self.tr("Spell Check"), self.tr("Spell check"),
            self.tr("Site"),
            self.tr("Start"), self.tr("start"), self.tr("START"),
            self.tr("Stop"), self.tr("stop"), self.tr("STOP"),
            self.tr("Submit"),
            self.tr("Translate"),
            self.tr("Transcode"),
            self.tr("Test"),
            self.tr("Type"),
            self.tr("Quit"),
            self.tr("Update"),
            self.tr("Update {0}"),

            self.tr("Less"),
            self.tr("More"),
            self.tr("No more"),

            self.tr("Replies"),
            self.tr("No replies"),

            # Articles
            self.tr("All files"),
            self.tr("Executable"), self.tr("Executables"),
            self.tr("Picture"), self.tr("Pictures"),
            self.tr("Shortcuts"),

            self.tr("All languages"),

            self.tr("Blue"),
            self.tr("Purple"),

            self.tr("Score"),
            self.tr("Slogan"),

            self.tr("Comiket"),

            self.tr("Article"), self.tr("article"),
            self.tr("Solved"), self.tr("solved"),

            self.tr("Scenario"),
            self.tr("Music"),

            self.tr("Machine Translation"),

            self.tr("Keyboard shortcuts"),

            self.tr("Otome"),

            self.tr("Asc"), self.tr("asc"),
            self.tr("Ascending"),
            self.tr("Desc"), self.tr("desc"),
            self.tr("Descending"),

            self.tr("Up"),
            self.tr("Down"),
            self.tr("Left"),
            self.tr("Right"),

            self.tr("Male"),
            self.tr("Female"),

            self.tr("Hiragana"),
            self.tr("Katagana"),
            self.tr("Romaji"), self.tr("romaji"),
            self.tr("Kanji"),
            self.tr("Kana"),
            self.tr("Pinyin"),

            self.tr("Hanja"),
            self.tr("Romaja"),

            self.tr("CG"),
            self.tr("Brand"), self.tr("brand"),
            self.tr("Label"), self.tr("label"),
            self.tr("Series"), self.tr("series"),

            self.tr("Visit"),
            self.tr("Visits"),

            self.tr("Year"),
            self.tr("Month"),
            self.tr("Day"),

            self.tr("Alphabet"),
            self.tr("All"), self.tr("all"),
            self.tr("Age"),
            self.tr("Aside"),
            self.tr("Author"),
            self.tr("Authors"),
            # self.tr("Auto"),
            self.tr("Automatic"),
            self.tr("Avatar"),
            self.tr("Background"),
            self.tr("Column"),
            self.tr("Cover"),
            self.tr("Creator"),
            self.tr("Creation Time"), self.tr("Creation time"),
            self.tr("Credits"),
            self.tr("Color"),
            self.tr("Content"),
            self.tr("Contents"),
            self.tr("Context"),
            self.tr("Context menu"), self.tr("context menu"),
            self.tr("Date"), self.tr("date"),
            self.tr("Desktop"),
            self.tr("Dictionary"),
            self.tr("Dictionaries"),
            self.tr("Default"), self.tr("default"),
            self.tr("Draft"),
            self.tr("Encoding"),
            self.tr("Error"), self.tr("error"),
            self.tr("Feature"),
            self.tr("Features"),
            self.tr("File"),
            self.tr("File size"),
            self.tr("Folder"),
            self.tr("Font"),
            self.tr("Font family"),
            self.tr("Fonts"),
            self.tr("Game"), self.tr("game"),
            self.tr("Game Information"), self.tr(
                "Game information"), self.tr("game information"),
            self.tr("Gender"),
            self.tr("Genre"),
            self.tr("Guest"),
            self.tr("Help"),
            self.tr("Homepage"),
            self.tr("Icon"),
            self.tr("Image"),
            self.tr("Images"),
            self.tr("Information"),
            self.tr("International"),
            self.tr("Internet error"),
            self.tr("Internet status"),
            self.tr("i18n"),
            self.tr("Keyboard"),
            self.tr("Keyword"),
            self.tr("Keywords"),
            self.tr("Lang"), self.tr("lang"),
            self.tr("Language"), self.tr("language"),
            self.tr("Languages"), self.tr("languages"),
            self.tr("Local"),
            self.tr("Locale"),
            self.tr("Location"),
            self.tr("Locations"),
            self.tr("Macro"),
            self.tr("Menu"),
            self.tr("News"), self.tr("news"),
            self.tr("Method"),
            self.tr("Name"),
            self.tr("Mouse"),
            self.tr("Notification"),
            self.tr("Opacity"),
            self.tr("Option"), self.tr("option"),
            self.tr("Optional"), self.tr("optional"),
            self.tr("Options"), self.tr("options"),
            self.tr("Order"),
            self.tr("Owner"),
            self.tr("Padding"),
            self.tr("Password"),
            self.tr("Pattern"),
            self.tr("Phrase"),
            self.tr("Pitch"),
            self.tr("Preferences"),
            self.tr("Price"),
            self.tr("Primary"), self.tr("primary"),
            self.tr("Priority"),
            self.tr("Privilege"),
            self.tr("Property"),
            self.tr("Properties"),
            self.tr("Proxy"),
            self.tr("Plug-in"),
            self.tr("Plug-ins"),
            self.tr("Question"), self.tr("question"),
            self.tr("Reference"),
            self.tr("References"),
            self.tr("Regular Expression"), self.tr(
                "Regular expression"), self.tr("regular expression"),
            self.tr("Regex"), self.tr("regex"),
            self.tr("Regexp"), self.tr("regexp"),
            self.tr("Rate"),
            self.tr("Rating"),
            self.tr("Release"),
            self.tr("Release Date"), self.tr("Release date"),
            self.tr("Review"), self.tr("review"),
            self.tr("Role"),
            self.tr("Row"),
            # self.tr("Scratch"),
            # self.tr("Subject"),
            self.tr("Screen"),
            self.tr("Screenshot"),
            self.tr("Script"),
            self.tr("Scripts"),
            self.tr("Settings"),
            self.tr("Size"),
            self.tr("Statistics"),
            self.tr("Status"),
            self.tr("Syntax"),
            self.tr("Tab"),
            self.tr("Target"),
            self.tr("Text"),
            self.tr("Text encoding"),
            self.tr("Theme"),
            self.tr("Themes"),
            self.tr("Title"), self.tr("title"),
            self.tr("Timestamp"),
            self.tr("Time zone"),
            self.tr("Topic"), self.tr("topic"),
            self.tr("Translation"),
            self.tr("Translator"),
            self.tr("Translators"),
            self.tr("UI"),
            self.tr("Unlock"), self.tr("unlock"),
            self.tr("Unlocked"), self.tr("unlocked"),
            self.tr("Update Time"), self.tr("Update time"),
            self.tr("User"), self.tr("user"),
            self.tr("User Information"), self.tr(
                "User information"), self.tr("user information"),
            self.tr("Users"), self.tr("users"),
            self.tr("Username"),
            self.tr("Volume"),
            self.tr("Wallpaper"),
            self.tr("Warn"),
            self.tr("Warning"),
            self.tr("Width"),
            self.tr("Window"), self.tr("window"),
            self.tr("Window title"),
            self.tr("Wiki"),
            self.tr("Wikipedia"),
            self.tr("Version"),
            self.tr("Zoom"),
            self.tr("Zoom In"), self.tr("Zoom in"),
            self.tr("Zoom Out"), self.tr("Zoom out"),

            # Status
            self.tr("Yes"), self.tr("yes"),
            self.tr("No"), self.tr("no"),
            self.tr("Online"), self.tr("online"),
            self.tr("Offline"), self.tr("offline"),
            self.tr("Read-only"), self.tr("read-only"),
            self.tr("Editable"), self.tr("editable"),

            self.tr("Required"), self.tr("required"),

            self.tr("Draggable"),

            self.tr("Unsaved"), self.tr("unsaved"),

            self.tr("Recent"),
            self.tr("Like"),
            self.tr("Dislike"),

            self.tr("Agree"),
            self.tr("Disagree"),

            self.tr("Slow"), self.tr("slow"),

            self.tr("Public"),
            self.tr("Private"),

            self.tr("Not changed"), self.tr("not changed"),

            self.tr("Case-sensitive"), self.tr("case-sensitive"),
            self.tr("Case-insensitive"), self.tr("case-insensitive"),
            self.tr("Ignore Case"), self.tr("Ignore case"),

            # Errors
            self.tr("Network Error"),

            # Messages
            self.tr("Found"),
            self.tr("Not found"),
            self.tr("Not specified"), self.tr("not specified"),

            self.tr("System default"),

            self.tr("Invalid"),

            self.tr("Press Enter to submit"),

            self.tr("Unknown"), self.tr("unknown"),

            self.tr("Unknown error"),
            self.tr("Unknown warning"),

            self.tr("Administrator"),
            self.tr("Not administrator"),

            self.tr("For example"), self.tr("for example"),

            self.tr("Check for updates"),

            # self.tr("Matched"),
            #self.tr("Not matched"),

            # Visual novel specific
            self.tr("Subtitle"), self.tr("subtitle"),
            self.tr("Subtitles"), self.tr("subtitles"),
            self.tr("Subs"), self.tr("subs"),
            self.tr("Comment"), self.tr("comment"),
            self.tr("Comments"), self.tr("comments"),
            self.tr("Danmaku"), self.tr("danmaku"),
            self.tr("Translation"), self.tr("translation"),
            self.tr("Text"), self.tr("text"),

            self.tr("Translate language"),
        )


@memoized
def manager(): return sakurakit()


def tr_(text): 
  """调用pyside中的tr函数让text转unicode格式，py3中可能不再需要"""
  return manager().tr(text)  # str -> unicode


def notr_(text): 
  """text原样返回不做转换"""
  return text     # any -> any


def utr_(text): 
  """unicode to unicode, py3中可能不再需要"""
  return tr_(text.encode(
    'utf8', errors='ignore'))  # unicode -> unicode

# EOF