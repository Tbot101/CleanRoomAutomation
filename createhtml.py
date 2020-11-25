import re
a = '''<!DOCTYPE html>
   <head>
      <title>GPIO Control</title>
      <link type="text/css" rel="stylesheet" href="/static/styles.css" id="stylespicker" title="Styles" />
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <!--<script src="/static/jquery.js"></script>-->
      <script src="/static/control.js"></script>
   </head>
   <body class="grid">
      <div class="left-column">
         <img src="/static/images/logo.png" class="logo">
         <div class="status">
         '''
sidebar = ""
for i in range(1,6):
    i1 = str(i)
    str1 = ('''<button class="room" id="roomCHANGENUMBERstyles" onclick="setRoom(CHANGENUMBER)">
               <div class="roomtitle">Room CHANGENUMBER</div>
               <div class="roomsensor">
                 {% if roomCHANGENUMBERlight == 1 %}
                 <img src="/static/images/lighton.png" class="utilityroomsensor">
                 {% else %}
                 <img src="/static/images/lightoff.png" class="utilityroomsensor">
                 {% endif %}

                 {% if roomCHANGENUMBERfan == 1 %}
                 <img src="/static/images/fanon.png" class="utilityroomsensor">
                 {% else %}
                 <img src="/static/images/fanoff.png" class="utilityroomsensor">
                 {% endif %}

                 {% if roomCHANGENUMBERaircon == 1 %}
                 <img src="/static/images/airconon.png" class="utilityroomsensor">
                 {% else %}
                 <img src="/static/images/airconoff.png" class="utilityroomsensor">
                 {% endif %}
               </div>
            </button>
            ''')
    str1formatted = re.sub("CHANGENUMBER", i1, str1)
    sidebar += str1formatted

b = ('''</div>
      </div>
      ''')
main = ""
for i in range(1,6):
    i2 = str(i)
    str2 = ('''<div class="light roomCHANGENUMBER">
        <h3>Light</h3>
        {% if roomCHANGENUMBERlight == 1 %}
        <img src="/static/images/lighton.png" class="utility">
        <div class="onoff">
          <a href="/roomCHANGENUMBERlight/on"class="button light_on_button_on">ON</a>
          <a href="/roomCHANGENUMBERlight/off" class="button light_off_button_off">OFF</a>
        </div>
        {% else %}
        <img src="/static/images/lightoff.png" class="utility">
        <div class="onoff">
          <a href="/roomCHANGENUMBERlight/on" class="button light_on_button_off">ON</a>
          <a href="/roomCHANGENUMBERlight/off" class="button light_off_button_on">OFF</a>
        </div>
        {% endif %}
        <div class="roomnumber">ROOM CHANGENUMBER</div>
      </div>
      <div class="fan roomCHANGENUMBER">
        <h3>Fan</h3>
        <div>
          {% if roomCHANGENUMBERfan == 1 %}
          <img src="/static/images/fanon.png" class="utility">
          <div class="onoff">
            <a href="/roomCHANGENUMBERfan/on" class="button fan_on_button_on">ON</a>
            <a href="/roomCHANGENUMBERfan/off" class="button fan_off_button_off">OFF</a>
          </div>
          <div>
            <form method="POST" action="/fanslider/roomCHANGENUMBER" id="roomCHANGENUMBERfanform" class="slidecontainer" onsubmit="setroomValue(CHANGENUMBER)">
              <input type="image" src="/static/images/decrease.png" value="-" onclick="buttonChange(-1, CHANGENUMBER)" class="decincbutton"/>
              <input type="image" src="/static/images/increase.png" value="+" onclick="buttonChange(1, CHANGENUMBER)" class="decincbutton"/>
              <input type="range" min="0" max="100" step="10" value="0" class="slider" name="Room_CHANGENUMBER_Fan_Slider" id="roomCHANGENUMBERfanslider"/>
            </form>
          </div>
          {% else %}
          <img src="/static/images/fanoff.png" class="utility">
          <div class="onoff">
            <a href="/roomCHANGENUMBERfan/on" class="button fan_on_button_off">ON</a>
            <a href="/roomCHANGENUMBERfan/off" class="button fan_off_button_on">OFF</a>
          </div>
          {% endif %}
        </div>
      </div>
      <div class="aircon roomCHANGENUMBER">
         <h3>Air Conditioner</h3>
         {% if roomCHANGENUMBERaircon == 1 %}
         <img src="/static/images/airconon.png" class="utility">
         <div class="onoff">
            <a href="/roomCHANGENUMBERaircon/on" class="button aircon_on_button_on">ON</a>
            <a href="/roomCHANGENUMBERaircon/off" class="button aircon_off_button_off">OFF</a>
          </div>
          <div class="airconstats">
            <div class="settemp">
                <p class="settempheader">SET TEMP</p>
                <input type="number" value="22" minimum="19" maximum="30" class="qty" id="roomCHANGENUMBERsettemp">
                <p class="degrees">C</p>
                <input type="image" src="/static/images/increase.png" onclick="airConEdit(CHANGENUMBER, 1); settempvalue(CHANGENUMBER); getairconsignal(CHANGENUMBER); " class="qty-plus settempbutton">
                <input type="image" src="/static/images/decrease.png" onclick="airConEdit(CHANGENUMBER, -1); settempvalue(CHANGENUMBER); getairconsignal(CHANGENUMBER); " class="qty-minus settempbutton">
            </div>
            <div class="fanspeed">
                <div>
                    <p class="fanspeedheader">FAN SPEED</p>
                    <input type="image" src="/static/images/fanlow.png" class="fanspeedimage" id="fanspeedimageroomCHANGENUMBER">
                </div>
                <div class="fanspeedbuttonwrapper">
                    <input type="image" src="/static/images/increase.png" class="fanspeedbutton" onclick="fanhigh(CHANGENUMBER); setfanvalue(CHANGENUMBER); getairconsignal(CHANGENUMBER)">
                    <input type="image" src="/static/images/decrease.png" class="fanspeedbutton" onclick="fanlow(CHANGENUMBER); setfanvalue(CHANGENUMBER); getairconsignal(CHANGENUMBER)">
                </div>
            </div>
            <div class="airconmodebuttonwrapper">
              <p class="airconmodeheader">Mode</p>
              <div class="airconmode" id="airconmodeCHANGENUMBER">
                <button value="AUTO" class="airconmodebutton" id="airconmodebuttonCHANGENUMBER1" onclick="airconmodeformat(CHANGENUMBER, CHANGENUMBER1); setairconvalue(CHANGENUMBER, CHANGENUMBER1); getairconsignal(CHANGENUMBER)">Auto</button>
                <button value="COOL" class="airconmodebutton" id="airconmodebuttonCHANGENUMBER2" onclick="airconmodeformat(CHANGENUMBER, CHANGENUMBER2); setairconvalue(CHANGENUMBER, CHANGENUMBER2); getairconsignal(CHANGENUMBER)">Cool</button>
                <button value="FAN" class="airconmodebutton" id="airconmodebuttonCHANGENUMBER3" onclick="airconmodeformat(CHANGENUMBER, CHANGENUMBER3); setairconvalue(CHANGENUMBER, CHANGENUMBER3); getairconsignal(CHANGENUMBER)">Fan</button>
              </div>
            </div>
          </div>
          {% else %}
          <img src="/static/images/airconoff.png" class="utility">
          <div class="onoff">
              <a href="/roomCHANGENUMBERaircon/on" class="button aircon_on_button_off">ON</a>
              <a href="/roomCHANGENUMBERaircon/off" class="button aircon_off_button_on">OFF</a>
          </div>
          {% endif %}
      </div>
      ''')
    
    str2formatted = re.sub("CHANGENUMBER", i2, str2)
    main += str2formatted

c = ('''
      </div>
   </body>
</html>
''')

with open('/home/pi/Documents/GitHub/CleanRoomAutomation/main.html', 'w') as newHTMLFile:
    newHTMLFile.write(a + sidebar + b + main + c)
    newHTMLFile.close()
