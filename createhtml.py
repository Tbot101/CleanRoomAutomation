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
         <div class="status">'''
sidebar = ""
for i in range(3):
    str1 = ('''<button class="room" id=f"room{i}styles" onclick=f"setRoom({i})">
               <div class="roomtitle">Room f"{i}"</div>
               <div class="roomsensor">
                 {% if roomf"{i}"light == 1 %}
                 <img src="/static/images/lighton.png" class="utilityroomsensor">
                 {% else %}
                 <img src="/static/images/lightoff.png" class="utilityroomsensor">
                 {% endif %}

                 {% if room1fan == 1 %}
                 <img src="/static/images/fanon.png" class="utilityroomsensor">
                 {% else %}
                 <img src="/static/images/fanoff.png" class="utilityroomsensor">
                 {% endif %}

                 {% if room1aircon == 1 %}
                 <img src="/static/images/airconon.png" class="utilityroomsensor">
                 {% else %}
                 <img src="/static/images/airconoff.png" class="utilityroomsensor">
                 {% endif %}
               </div>
            </button>
            ''')
    sidebar += str1

b = ('''</div>
      </div>
      ''')
main = ""
for i in range(3):
    str2 = ('''<div class=f"light room{i}">
        <h3>Light</h3>
        {% if room1light == 1 %}
        <img src="/static/images/lighton.png" class="utility">
        <div class="onoff">
          <a href="/room1light/on"class="button light_on_button_on">ON</a>
          <a href="/room1light/off" class="button light_off_button_off">OFF</a>
        </div>
        {% else %}
        <img src="/static/images/lightoff.png" class="utility">
        <div class="onoff">
          <a href="/room1light/on" class="button light_on_button_off">ON</a>
          <a href="/room1light/off" class="button light_off_button_on">OFF</a>
        </div>
        {% endif %}
        <div class="roomnumber">ROOM f"{i}"</div>
      </div>
      <div class="fan room1">
        <h3>Fan</h3>
        <div>
          {% if room1fan == 1 %}
          <img src="/static/images/fanon.png" class="utility">
          <div class="onoff">
            <a href="/room1fan/on" class="button fan_on_button_on">ON</a>
            <a href="/room1fan/off" class="button fan_off_button_off">OFF</a>
          </div>
          <div>
            <form method="POST" action="/fanslider/room1" id="room1fanform" class="slidecontainer" onsubmit="setroomValue(1)">
              <input type="image" src="/static/images/decrease.png" value="-" onclick="buttonChange(-1, 1)" class="decincbutton"/>
              <input type="image" src="/static/images/increase.png" value="+" onclick="buttonChange(1, 1)" class="decincbutton"/>
              <input type="range" min="0" max="100" step="10" value="0" class="slider" name="Room_1_Fan_Slider" id="room1fanslider"/>
            </form>
          </div>
          {% else %}
          <img src="/static/images/fanoff.png" class="utility">
          <div class="onoff">
            <a href="/room1fan/on" class="button fan_on_button_off">ON</a>
            <a href="/room1fan/off" class="button fan_off_button_on">OFF</a>
          </div>
          {% endif %}
        </div>
      </div>
      <div class="aircon room1">
         <h3>Air Conditioner</h3>
         {% if room1aircon == 1 %}
         <img src="/static/images/airconon.png" class="utility">
         <div class="onoff">
            <a href="/room1aircon/on" class="button aircon_on_button_on">ON</a>
            <a href="/room1aircon/off" class="button aircon_off_button_off">OFF</a>
          </div>
          <div class="airconstats">
            <div class="settemp">
                <p class="settempheader">SET TEMP</p>
                <input type="number" value="22" minimum="19" maximum="30" class="qty" id="room1settemp">
                <p class="degrees">C</p>
                <input type="image" src="/static/images/increase.png" onclick="airConEdit(1, 1); settempvalue(1); getairconsignal(1); " class="qty-plus settempbutton">
                <input type="image" src="/static/images/decrease.png" onclick="airConEdit(1, -1); settempvalue(1); getairconsignal(1); " class="qty-minus settempbutton">
            </div>
            <div class="fanspeed">
                <div>
                    <p class="fanspeedheader">FAN SPEED</p>
                    <input type="image" src="/static/images/fanlow.png" class="fanspeedimage" id="fanspeedimageroom1">
                </div>
                <div class="fanspeedbuttonwrapper">
                    <input type="image" src="/static/images/increase.png" class="fanspeedbutton" onclick="fanhigh(1); setfanvalue(1); getairconsignal(1)">
                    <input type="image" src="/static/images/decrease.png" class="fanspeedbutton" onclick="fanlow(1); setfanvalue(1); getairconsignal(1)">
                </div>
            </div>
            <div class="airconmodebuttonwrapper">
              <p class="airconmodeheader">Mode</p>
              <div class="airconmode" id="airconmode1">
                <button value="AUTO" class="airconmodebutton" id="airconmodebutton11" onclick="airconmodeformat(1, 11); setairconvalue(1, 11); getairconsignal(1)">Auto</button>
                <button value="COOL" class="airconmodebutton" id="airconmodebutton12" onclick="airconmodeformat(1, 12); setairconvalue(1, 12); getairconsignal(1)">Cool</button>
                <button value="FAN" class="airconmodebutton" id="airconmodebutton13" onclick="airconmodeformat(1, 13); setairconvalue(1, 13); getairconsignal(1)">Fan</button>
              </div>
            </div>
          </div>
          {% else %}
          <img src="/static/images/airconoff.png" class="utility">
          <div class="onoff">
              <a href="/room1aircon/on" class="button aircon_on_button_off">ON</a>
              <a href="/room1aircon/off" class="button aircon_off_button_on">OFF</a>
          </div>
          {% endif %}
      </div>
      ''')

    main += str2

c = ('''
      </div>
   </body>
</html>
''')

with open('/home/pi/Documents/GitHub/CleanRoomAutomation/main.html', 'w') as newHTMLFile:
    newHTMLFile.write(a + sidebar + b + main + c)
    newHTMLFile.close()
