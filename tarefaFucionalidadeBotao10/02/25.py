<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1387</width>
    <height>528</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>-10</y>
      <width>541</width>
      <height>511</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>6</width>
      <height>6</height>
     </size>
    </property>
    <property name="sizeIncrement">
     <size>
      <width>23</width>
      <height>23</height>
     </size>
    </property>
    <property name="cursor">
     <cursorShape>CrossCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(85, 255, 127);</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::Shape::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Shadow::Raised</enum>
    </property>
    <widget class="QFrame" name="usuario">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>150</y>
       <width>511</width>
       <height>41</height>
      </rect>
     </property>
     <property name="frameShape">
      <enum>QFrame::Shape::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Shadow::Raised</enum>
     </property>
     <widget class="QLabel" name="usuario_3">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>49</width>
        <height>16</height>
       </rect>
      </property>
      <property name="text">
       <string>Usuario</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="digit_seu_usuario">
      <property name="geometry">
       <rect>
        <x>70</x>
        <y>10</y>
        <width>361</width>
        <height>22</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
     <widget class="QFrame" name="usuario_2">
      <property name="geometry">
       <rect>
        <x>430</x>
        <y>40</y>
        <width>511</width>
        <height>41</height>
       </rect>
      </property>
      <property name="frameShape">
       <enum>QFrame::Shape::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Shadow::Raised</enum>
      </property>
      <widget class="QLabel" name="label_2">
       <property name="geometry">
        <rect>
         <x>10</x>
         <y>10</y>
         <width>49</width>
         <height>16</height>
        </rect>
       </property>
       <property name="text">
        <string>Usuario</string>
       </property>
      </widget>
      <widget class="QLineEdit" name="lineEdit_2">
       <property name="geometry">
        <rect>
         <x>70</x>
         <y>10</y>
         <width>361</width>
         <height>22</height>
        </rect>
       </property>
      </widget>
     </widget>
    </widget>
    <widget class="QFrame" name="senha_fre">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>290</y>
       <width>511</width>
       <height>41</height>
      </rect>
     </property>
     <property name="frameShape">
      <enum>QFrame::Shape::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Shadow::Raised</enum>
     </property>
     <widget class="QLabel" name="senha">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>10</y>
        <width>49</width>
        <height>16</height>
       </rect>
      </property>
      <property name="text">
       <string>senha</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="digit_senha">
      <property name="geometry">
       <rect>
        <x>70</x>
        <y>10</y>
        <width>361</width>
        <height>22</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
     <widget class="QFrame" name="usuario_4">
      <property name="geometry">
       <rect>
        <x>430</x>
        <y>40</y>
        <width>511</width>
        <height>41</height>
       </rect>
      </property>
      <property name="frameShape">
       <enum>QFrame::Shape::StyledPanel</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Shadow::Raised</enum>
      </property>
      <widget class="QLabel" name="label_4">
       <property name="geometry">
        <rect>
         <x>10</x>
         <y>10</y>
         <width>49</width>
         <height>16</height>
        </rect>
       </property>
       <property name="text">
        <string>Usuario</string>
       </property>
      </widget>
      <widget class="QLineEdit" name="lineEdit_4">
       <property name="geometry">
        <rect>
         <x>70</x>
         <y>10</y>
         <width>361</width>
         <height>22</height>
        </rect>
       </property>
      </widget>
     </widget>
    </widget>
    <widget class="QLabel" name="login">
     <property name="geometry">
      <rect>
       <x>160</x>
       <y>40</y>
       <width>161</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Myanmar Text</family>
       <pointsize>22</pointsize>
      </font>
     </property>
     <property name="text">
      <string>Login</string>
     </property>
    </widget>
    <zorder>login</zorder>
    <zorder>senha_fre</zorder>
    <zorder>usuario</zorder>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="ale03.ui"/>
  <include location="santos.qrc"/>
 </resources>
 <connections/>
</ui>
