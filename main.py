from kivymd.app import MDApp
from kivy.lang import  Builder
from kivymd.uix.button import MDIconButton
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import  ObjectProperty
from kivymd.toast import  toast
from Game import Game
import  requests
from kivymd.uix.snackbar import Snackbar

root_kv=('''
<IconButton@MDIconButton+ToggleButtonBehavior>:
	
MDFloatLayout:
	canvas:
		Color:
			rgba:91/255.0,188/255.0,228/255.0,1
		Rectangle:
			size:self.size
			pos:self.pos
	MDCard:
		size_hint:None,None
		size:('300dp','450dp')
		padding:'8dp'
		elevation:8
		focus_behavior:1
		ripple_behavior:1
		border_radius: 30
        radius: [30]
		pos_hint:{"center_x":0.5,"center_y":0.5}
		MDFloatLayout:
			MDLabel:
				text:'LOGIN'
				bold:True
				theme_text_color:'Custom'
				text_color:0,0,0,1
				height:self.texture_size[1] 
				valign:'middle'
				font_style:'H4'
				halign:'center'
				pos_hint:{'center_x':0.5,'y':0.43}
			MDLabel:
				text:'Email Address :'
			    valign:'middle' 
				halign:'left'
		    	theme_text_color:'Custom'
				text_color:0.56,0,1,1
				height:self.texture_size[1] 
				pos_hint:{'x':0.0,'y':0.33}
				padding_x:dp(7)
		
			MDTextField:
				id:email
				hint_text:'please enter your email id'
		        required:True
				color_mode:'custom'
				mode:'line'
				icon_right:'account'
				line_color_focus:1,0.35,1,1
				line_anim:1
				pos_hint:{'x':0.027,'center_y':0.75}		
		    MDLabel:
			    text:'Password:'
			    valign:'middle' 
				halign:'left'
		    	theme_text_color:'Custom'
				text_color:0.56,0,1,1
				height:self.texture_size[1] 			
				padding_x:dp(7)
		        pos_hint:{'x':0.0,'y':0.16}
			MDTextField:
				id:pass_word
				hint_text:'please enter your password:'			    		
				required:True
				color_mode:'custom'
				mode:'line'
				line_color_focus:1,0.35,1,1
				line_anim:1			
				password:True
				pos_hint:{'x':0.027,'center_y':0.57}	
	
			IconToggleButton:
				id:toggle_btn
				icon:{'normal':'./eye.png','down':'./visibility-button.png'}[self.state]
				size:45,45
				size_hint:None,None
				on_state:root.func()
				pos_hint:{'right':1,'center_y':0.6}
		    Button:
				size_hint:0.4,0.2				
				background_normal:'./Login_btn.png'
				background_down:'./Login_btn.png'
				allow_stretch:True
				on_press:root.login_func()
				pos_hint:{'center_x':0.5,'center_y':0.42}
			MDTextButton:
				text:'Forgot Password'
				font_size:dp(18)
				underline:True
				pos_hint:{'center_x':0.5,'center_y':0.3}					
			MDTextButton:
			    text:'Registration Here'
				font_size:dp(18)
				bold:True
				pos_hint:{'center_x':0.5,'center_y':0.2}
			MDTextButton:
			    text:'Skip Login'
				font_size:dp(16)
				underline:True
				pos_hint:{'center_x':0.5,'center_y':0.1}
				on_press:app.skip()

				''')
class IconToggleButton(ToggleButtonBehavior, MDIconButton):
	def __init__(self, **kwargs):
		super(IconToggleButton, self).__init__()
	

class login(MDApp):
	def __init__(self, **kwargs):
		self.title = "ColourHub"
		self.auth='JvMoJBZZP1EBkYVeGvVmN2gLhTZcFjUfajXJcvEd'
		self.url='https://database-kivy-default-rtdb.firebaseio.com/.json'	
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "DeepPurple"
		super().__init__(**kwargs)

	def build(self):
		self.root = Builder.load_string(root_kv)
		
	def func(self):
		boolval=self.root.ids.pass_word.password
		if boolval==True:
			self.root.ids.pass_word.password=False
		else:
			self.root.ids.pass_word.password=True
	def  login_func(self):
		email=self.root.ids.email.text
		password=self.root.ids.pass_word.text
		email=email.replace('.','-')
		password=password.replace('.','-')
		req=requests.get(url=self.url+'?auth='+self.auth)
		data=req.json()
		email_set=set()
		password_set=set()
		username=set()
		name=set()
		for key,value in data.items():
			email_set.add(key)
			password_set.add(value['password'])
			username.add(value['Username'])
			name.add(value['Name'])
		print(name)
		if email in email_set and password in password_set or email in username:
			Game().run()
		else:
			snackbar=Snackbar(text="Invalid Email/Username & Password")
			snackbar.show()
			
	def skip(self):
	    toast('pass')
			
if __name__=='__main__':
	login().run()
