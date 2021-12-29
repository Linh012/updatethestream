ui_string = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>udts</class>
 <widget class="QMainWindow" name="udts">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Someone, Update The Stream!</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>
      <height>600</height>
     </rect>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="live_tab">
     <attribute name="title">
      <string>Live</string>
     </attribute>
     <widget class="QWidget" name="verticalLayoutWidget">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>160</width>
        <height>80</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="startstop_vbox">
       <item>
        <widget class="QPushButton" name="start_button">
         <property name="enabled">
          <bool>false</bool>
         </property>
         <property name="toolTip">
          <string>Starts the tournament with all current configuration. Writes out OBS files to disk.</string>
         </property>
         <property name="text">
          <string>Start (Not Implemented)</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="stop_button">
         <property name="enabled">
          <bool>false</bool>
         </property>
         <property name="toolTip">
          <string>Stops the tournament. All progress will be lost.</string>
         </property>
         <property name="text">
          <string>Stop (Not Implemented)</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QGroupBox" name="groupBox">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>120</y>
        <width>790</width>
        <height>410</height>
       </rect>
      </property>
      <property name="title">
       <string>Tournament In Progress:</string>
      </property>
      <widget class="QWidget" name="verticalLayoutWidget_3">
       <property name="geometry">
        <rect>
         <x>250</x>
         <y>40</y>
         <width>21</width>
         <height>71</height>
        </rect>
       </property>
       <layout class="QVBoxLayout" name="round_score_vbox">
        <item>
         <widget class="QLabel" name="team1_score_label">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="text">
           <string>0</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QLabel" name="team2_score_label">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="text">
           <string>0</string>
          </property>
          <property name="alignment">
           <set>Qt::AlignCenter</set>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QLabel" name="final_score_label">
       <property name="geometry">
        <rect>
         <x>190</x>
         <y>20</y>
         <width>61</width>
         <height>20</height>
        </rect>
       </property>
       <property name="text">
        <string>Final Score</string>
       </property>
      </widget>
      <widget class="QWidget" name="verticalLayoutWidget_2">
       <property name="geometry">
        <rect>
         <x>10</x>
         <y>40</y>
         <width>170</width>
         <height>70</height>
        </rect>
       </property>
       <layout class="QVBoxLayout" name="win_controls_vbox">
        <item>
         <widget class="QPushButton" name="team1_win_button">
          <property name="text">
           <string>TSM Win</string>
          </property>
         </widget>
        </item>
        <item>
         <widget class="QPushButton" name="team2_win_button">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
            <horstretch>0</horstretch>
            <verstretch>0</verstretch>
           </sizepolicy>
          </property>
          <property name="text">
           <string>CLG Win</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QLabel" name="now_playing_label">
       <property name="geometry">
        <rect>
         <x>70</x>
         <y>20</y>
         <width>80</width>
         <height>15</height>
        </rect>
       </property>
       <property name="text">
        <string>Current Match</string>
       </property>
      </widget>
      <widget class="QLabel" name="standings_label">
       <property name="geometry">
        <rect>
         <x>670</x>
         <y>20</y>
         <width>50</width>
         <height>15</height>
        </rect>
       </property>
       <property name="text">
        <string>Standings</string>
       </property>
      </widget>
      <widget class="QLabel" name="schedule_label">
       <property name="geometry">
        <rect>
         <x>400</x>
         <y>20</y>
         <width>50</width>
         <height>15</height>
        </rect>
       </property>
       <property name="text">
        <string>Schedule</string>
       </property>
      </widget>
      <widget class="QWidget" name="formLayoutWidget_5">
       <property name="geometry">
        <rect>
         <x>10</x>
         <y>110</y>
         <width>260</width>
         <height>280</height>
        </rect>
       </property>
       <layout class="QFormLayout" name="info_form">
        <property name="leftMargin">
         <number>5</number>
        </property>
        <property name="topMargin">
         <number>5</number>
        </property>
        <item row="1" column="0">
         <widget class="QLabel" name="best_of_label">
          <property name="text">
           <string>Best of:</string>
          </property>
         </widget>
        </item>
        <item row="1" column="1">
         <widget class="QLabel" name="best_of_count_label">
          <property name="text">
           <string>5</string>
          </property>
         </widget>
        </item>
        <item row="2" column="0">
         <widget class="QLabel" name="up_next_label">
          <property name="text">
           <string>Up Next:</string>
          </property>
         </widget>
        </item>
        <item row="2" column="1">
         <widget class="QLabel" name="up_next_match">
          <property name="text">
           <string>PGG vs IMAY</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QListWidget" name="schedule_list_widget">
       <property name="geometry">
        <rect>
         <x>280</x>
         <y>40</y>
         <width>310</width>
         <height>350</height>
        </rect>
       </property>
      </widget>
      <widget class="QListWidget" name="standings_list_widget">
       <property name="geometry">
        <rect>
         <x>595</x>
         <y>40</y>
         <width>190</width>
         <height>350</height>
        </rect>
       </property>
      </widget>
      <widget class="QWidget" name="verticalLayoutWidget_4">
       <property name="geometry">
        <rect>
         <x>180</x>
         <y>40</y>
         <width>70</width>
         <height>70</height>
        </rect>
       </property>
       <layout class="QVBoxLayout" name="game_score_vbox">
        <property name="leftMargin">
         <number>5</number>
        </property>
        <property name="rightMargin">
         <number>5</number>
        </property>
        <item>
         <widget class="QLineEdit" name="team1_final_score_field"/>
        </item>
        <item>
         <widget class="QLineEdit" name="team2_final_score_field"/>
        </item>
       </layout>
      </widget>
     </widget>
     <widget class="QWidget" name="verticalLayoutWidget_5">
      <property name="geometry">
       <rect>
        <x>529</x>
        <y>10</y>
        <width>121</width>
        <height>80</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="undo_vbox">
       <item>
        <widget class="QPushButton" name="undo_button">
         <property name="toolTip">
          <string>In case of misclicking which team won, click this to roll back.</string>
         </property>
         <property name="text">
          <string>Undo Last Result</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QWidget" name="verticalLayoutWidget_6">
      <property name="geometry">
       <rect>
        <x>180</x>
        <y>10</y>
        <width>160</width>
        <height>80</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="refresh_vbox">
       <item>
        <widget class="QPushButton" name="refresh_ui_button">
         <property name="toolTip">
          <string>Update with configuration changes. Use this at your own risk.</string>
         </property>
         <property name="text">
          <string>Force Refresh UI</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="refresh_stream_button">
         <property name="toolTip">
          <string>Forcibly rewrites the stream labels to disk.</string>
         </property>
         <property name="text">
          <string>Force Refresh Stream</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QLabel" name="label">
      <property name="geometry">
       <rect>
        <x>650</x>
        <y>0</y>
        <width>120</width>
        <height>50</height>
       </rect>
      </property>
      <property name="text">
       <string/>
      </property>
      <property name="pixmap">
       <pixmap>chhtvlogo.png</pixmap>
      </property>
      <property name="scaledContents">
       <bool>true</bool>
      </property>
     </widget>
     <widget class="QLabel" name="label_2">
      <property name="geometry">
       <rect>
        <x>660</x>
        <y>40</y>
        <width>120</width>
        <height>20</height>
       </rect>
      </property>
      <property name="sizePolicy">
       <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
        <horstretch>0</horstretch>
        <verstretch>0</verstretch>
       </sizepolicy>
      </property>
      <property name="text">
       <string>esports for everyone</string>
      </property>
     </widget>
     <widget class="QWidget" name="verticalLayoutWidget_7">
      <property name="geometry">
       <rect>
        <x>370</x>
        <y>20</y>
        <width>131</width>
        <height>71</height>
       </rect>
      </property>
      <layout class="QVBoxLayout" name="swap_vbox">
       <item>
        <widget class="QPushButton" name="swap_button">
         <property name="toolTip">
          <string>Switch which sides teams are on.</string>
         </property>
         <property name="text">
          <string>Swap Red/Blue</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="blue_label">
         <property name="text">
          <string>Blue:</string>
         </property>
        </widget>
       </item>
        <item>
        <widget class="QLabel" name="red_label">
         <property name="text">
          <string>Red:</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </widget>
    <widget class="QWidget" name="teams_tab">
     <attribute name="title">
      <string>Teams</string>
     </attribute>
     <widget class="QWidget" name="formLayoutWidget">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>10</y>
        <width>190</width>
        <height>74</height>
       </rect>
      </property>
      <layout class="QFormLayout" name="add_team_form">
       <item row="0" column="0">
        <widget class="QLabel" name="add_team_name_label">
         <property name="text">
          <string>Name</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0">
        <widget class="QLabel" name="add_team_tricode_label">
         <property name="text">
          <string>Tricode</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QLineEdit" name="add_team_name_field">
         <property name="placeholderText">
          <string>e.g. Team Solo Mid</string>
         </property>
        </widget>
       </item>
       <item row="1" column="1">
        <widget class="QLineEdit" name="add_team_tricode_field">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="placeholderText">
          <string>e.g. TSM</string>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QLabel" name="add_team_points_label">
         <property name="text">
          <string>Points</string>
         </property>
        </widget>
       </item>
       <item row="2" column="1">
        <widget class="QLineEdit" name="add_team_points_field">
         <property name="text">
          <string/>
         </property>
         <property name="placeholderText">
          <string>e.g. 10</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QPushButton" name="add_team_button">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>75</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>Add Team</string>
      </property>
     </widget>
     <widget class="QWidget" name="formLayoutWidget_2">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>100</y>
        <width>190</width>
        <height>75</height>
       </rect>
      </property>
      <layout class="QFormLayout" name="edit_team_form">
       <item row="0" column="0">
        <widget class="QLabel" name="edit_team_name_label">
         <property name="text">
          <string>Name</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0">
        <widget class="QLabel" name="edit_team_tricode_label">
         <property name="text">
          <string>Tricode</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QLineEdit" name="edit_team_name_field">
         <property name="placeholderText">
          <string>e.g. Team Solo Mid</string>
         </property>
        </widget>
       </item>
       <item row="1" column="1">
        <widget class="QLineEdit" name="edit_team_tricode_field">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="placeholderText">
          <string>e.g. TSM</string>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QLabel" name="edit_team_points_label">
         <property name="text">
          <string>Points</string>
         </property>
        </widget>
       </item>
       <item row="2" column="1">
        <widget class="QLineEdit" name="edit_team_points_field">
         <property name="text">
          <string/>
         </property>
         <property name="placeholderText">
          <string>e.g. 10</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QPushButton" name="edit_team_button">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>100</y>
        <width>70</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>Save Edits</string>
      </property>
     </widget>
     <widget class="QPushButton" name="delete_team_button">
      <property name="enabled">
       <bool>false</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>220</x>
        <y>180</y>
        <width>70</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>Delete</string>
      </property>
     </widget>
     <widget class="QCheckBox" name="delete_team_confirm_checkbox">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>180</y>
        <width>90</width>
        <height>20</height>
       </rect>
      </property>
      <property name="text">
       <string>Confirm Delete</string>
      </property>
     </widget>
     <widget class="QListWidget" name="team_list_widget">
      <property name="geometry">
       <rect>
        <x>310</x>
        <y>10</y>
        <width>450</width>
        <height>500</height>
       </rect>
      </property>
      <property name="sizePolicy">
       <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
        <horstretch>0</horstretch>
        <verstretch>1</verstretch>
       </sizepolicy>
      </property>
      <item>
       <property name="text">
        <string/>
       </property>
      </item>
     </widget>
    </widget>
    <widget class="QWidget" name="matches_tab">
     <attribute name="title">
      <string>Matches</string>
     </attribute>
     <widget class="QPushButton" name="add_match_button">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>75</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>Add Match</string>
      </property>
     </widget>
     <widget class="QPushButton" name="delete_match_button">
      <property name="enabled">
       <bool>false</bool>
      </property>
      <property name="geometry">
       <rect>
        <x>220</x>
        <y>180</y>
        <width>70</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>Delete</string>
      </property>
     </widget>
     <widget class="QWidget" name="formLayoutWidget_3">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>100</y>
        <width>190</width>
        <height>75</height>
       </rect>
      </property>
      <layout class="QFormLayout" name="edit_match_form_layout">
       <item row="0" column="0">
        <widget class="QLabel" name="edit_match_team1_label">
         <property name="text">
          <string>Team 1</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0">
        <widget class="QLabel" name="edit_match_team2_label">
         <property name="text">
          <string>Team 2</string>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QLabel" name="edit_match_bestof_label">
         <property name="text">
          <string>Best Of</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QComboBox" name="edit_match_team1_dropdown">
         <property name="editable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item row="1" column="1">
        <widget class="QComboBox" name="edit_match_team2_dropdown">
         <property name="editable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item row="2" column="1">
        <widget class="QComboBox" name="edit_match_bestof_dropdown">
         <item>
          <property name="text">
           <string>1</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>3</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>5</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>7</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>9</string>
          </property>
         </item>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QListWidget" name="match_list_widget">
      <property name="geometry">
       <rect>
        <x>310</x>
        <y>10</y>
        <width>450</width>
        <height>500</height>
       </rect>
      </property>
     </widget>
     <widget class="QPushButton" name="edit_match_button">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>100</y>
        <width>70</width>
        <height>25</height>
       </rect>
      </property>
      <property name="text">
       <string>Save Edits</string>
      </property>
     </widget>
     <widget class="QWidget" name="formLayoutWidget_4">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>10</y>
        <width>190</width>
        <height>75</height>
       </rect>
      </property>
      <layout class="QFormLayout" name="add_match_form_layout">
       <item row="0" column="0">
        <widget class="QLabel" name="add_match_team1_label">
         <property name="text">
          <string>Team 1</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0">
        <widget class="QLabel" name="add_match_team2_label">
         <property name="text">
          <string>Team 2</string>
         </property>
        </widget>
       </item>
       <item row="2" column="0">
        <widget class="QLabel" name="add_match_bestof_label">
         <property name="text">
          <string>Best Of</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QComboBox" name="add_match_team1_dropdown">
         <property name="editable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item row="1" column="1">
        <widget class="QComboBox" name="add_match_team2_dropdown">
         <property name="editable">
          <bool>false</bool>
         </property>
        </widget>
       </item>
       <item row="2" column="1">
        <widget class="QComboBox" name="add_match_bestof_dropdown">
         <item>
          <property name="text">
           <string>1</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>3</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>5</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>7</string>
          </property>
         </item>
         <item>
          <property name="text">
           <string>9</string>
          </property>
         </item>
        </widget>
       </item>
      </layout>
     </widget>
     <widget class="QCheckBox" name="delete_match_confirm_checkbox">
      <property name="geometry">
       <rect>
        <x>100</x>
        <y>180</y>
        <width>90</width>
        <height>20</height>
       </rect>
      </property>
      <property name="text">
       <string>Confirm Delete</string>
      </property>
     </widget>
     <widget class="QWidget" name="horizontalLayoutWidget_2">
      <property name="geometry">
       <rect>
        <x>130</x>
        <y>210</y>
        <width>160</width>
        <height>41</height>
       </rect>
      </property>
      <layout class="QHBoxLayout" name="match_order_hbox_2">
       <item>
        <widget class="QPushButton" name="match_move_up_button">
         <property name="text">
          <string>Move Up</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="match_move_down_button">
         <property name="text">
          <string>Move Down</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuSomeone_Update_The_Stream">
    <property name="title">
     <string>File</string>
    </property>
    <addaction name="actionNew"/>
    <addaction name="actionOpen"/>
    <addaction name="actionSave"/>
    <addaction name="actionSaveAs"/>
    <addaction name="actionSaveState"/>
    <addaction name="actionSaveAsState"/>
    <addaction name="separator"/>
    <addaction name="actionExit"/>
   </widget>
   <widget class="QMenu" name="menuAbout">
    <property name="title">
     <string>About</string>
    </property>
    <addaction name="actionHelp"/>
   </widget>
   <addaction name="menuSomeone_Update_The_Stream"/>
   <addaction name="menuAbout"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="actionOpen">
   <property name="text">
    <string>Open</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+O</string>
   </property>
  </action>
  <action name="actionNew">
   <property name="text">
    <string>New</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+N</string>
   </property>
  </action>
  <action name="actionSaveAs">
   <property name="text">
    <string>Save As</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+Shift+S</string>
   </property>
  </action>
  <action name="actionSave">
   <property name="text">
    <string>Save</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+S</string>
   </property>
  </action>
  <action name="actionExit">
   <property name="text">
    <string>Exit</string>
   </property>
   <property name="shortcut">
    <string>Ctrl+Q</string>
   </property>
  </action>
  <action name="actionSaveState">
   <property name="text">
    <string>Save Tournament In Current State</string>
   </property>
  </action>
  <action name="actionSaveAsState">
   <property name="text">
    <string>Save Tournament In Current State As..</string>
   </property>
  </action>
  <action name="actionHelp">
   <property name="text">
    <string>tell me about this app, please</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
"""