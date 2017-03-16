# PythonMenuSetup
Simple cross platform menu setup for python 3 in terminal

This is a class that you can put in any of your python programs!
It allows you to simply create menues for your game/program and the class takes care of it all.
Here's how you create a menu:

	FirstMenu = menu(		#'FirstMenu' will be the name of your menu variable
		"Title.",		#This is your menu's headline that will be displayed in the terminal
		{
		"0":[			#This is the (0-based) number of your alternative the user can coose from. (Has to be a string!)
			"Alternative",	#This is the alternative itself that will be displayed in the terminal
			"SecondMenu"	#This is the variable name of the menu that will display if the user picks this alterative. (Has to be a string!) Put 0 (Not a string!) for no menu (exit)
			],
		"1":[
			"Alternative",
			"ThirdMenu"
			]
		}
	)

	FirstMenu.run()			#This starts an interactive visualization of your first menu and changes to the next menu based on the users choises!

The menu class is made so that you don't have to modify it in order to add menues, It takes care of the dirty work for you.
Hope this helped some of you when it comes to menu creation in python :)
