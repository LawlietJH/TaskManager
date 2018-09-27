
# Habilita o Deshabilita el Administrador de Tareas con Python.
# By: LawlietJH
# v1.2.0


import ctypes, sys
import winreg as _winreg


class TaskManager(object):
	
	
	DISABLE_KEY_LOCATION = "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System"
	
	
	def __init__(self): pass
	
	
	def disable(self):
		
		key_exists = False
		
		# Intenta leer el key.
		try:
			
			reg = _winreg.OpenKeyEx(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
			
			disabled = _winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
			
			_winreg.CloseKey(reg)
			
			key_exists = True
			
		except: pass
		
		# Si no existe el key, lo crea y lo deshabilita.
		if not key_exists:
			
			reg = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
			
			_winreg.SetValueEx(reg, "DisableTaskMgr", 0,  _winreg.REG_DWORD, 0x00000001)
			
			_winreg.CloseKey(reg)
			
			print("\n\n\t [+] El Administrador de Tareas se ha Deshabilitado.\n")
			
		# Si existe el key y esta habilitado, lo deshabilita.
		elif key_exists and not disabled:
			
			reg = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION, 0, _winreg.KEY_SET_VALUE)
			
			_winreg.SetValueEx(reg, "DisableTaskMgr", 0,  _winreg.REG_DWORD, 0x00000001)
			
			_winreg.CloseKey(reg)
			
			print("\n\n\t [+] El Administrador de Tareas se ha Deshabilitado.\n")
	
		else: print("\n\n\t [+] El Administrador de Tareas ya esta Deshabilitado.\n")
		
	def enable(self):
		
		key_exists = False
		
		# Intenta leer el key.
		try:
			
			reg = _winreg.OpenKeyEx(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION)
			
			disabled = _winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
			
			_winreg.CloseKey(reg)
			
			key_exists = True
			
		except: pass
			
		# Si existe el key y esta deshabilitado, lo habilita.
		if key_exists and disabled:
			
			reg = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, self.DISABLE_KEY_LOCATION, 0, _winreg.KEY_SET_VALUE)
			
			_winreg.SetValueEx(reg, "DisableTaskMgr", 0,  _winreg.REG_DWORD, 0x00000000)
			
			_winreg.CloseKey(reg)
			
			print("\n\n\t [+] El Administrador de Tareas se ha Habilitado.\n")
		
		else: print("\n\n\t [+] El Administrador de Tareas ya esta Habilitado.\n")
			



class User():
	
	# Función Que Permite Saber Si Se Tienen Permisos de Administrador.
	def isAdmin():
		
		xD = ctypes.windll.shell32.IsUserAnAdmin()
		
		return (True if xD == 1 else False)


ModoDeUso = """

 Modo de Uso:
 
 
    python TaskManager.py [ -e | -d ] | [-h]


    -h, --help          Muestra el Modo de Uso.


    -e, --enable        Habilita el Administrador de Tareas.
                        (Ctrl + Shift + Esc)

    -d, --disable       Deshabilita el Administrador de Tareas.
                        (Ctrl + Shift + Esc)
"""


if __name__ == "__main__":
	
	if User.isAdmin():
		
		TaskM = TaskManager()
		
		Args = sys.argv
		
		if len(Args) == 1: print("\n\n\t Requiere un Parametro:\n" + ModoDeUso)
		
		elif len(Args) == 2:
			
			if   Args[1] == '-h' or Args[1] == '--help':    print(ModoDeUso)
			elif Args[1] == '-e' or Args[1] == '--enable':  TaskM.enable()
			elif Args[1] == '-d' or Args[1] == '--disable': TaskM.disable()
			else: print("\n\n\t Parametro Incorrecto: "+ Args[1] +"\n" + ModoDeUso)
			
		else: print("\n\n\t Requiere un Solo Parametro:\n" + ModoDeUso)
		
	else: print("\n\n\t [!] Necesitas Permisos de Administrador.\n")
	
	
	#===================================================================
	
	
	# Este Script Requiere permisos de Administrador, abre una ventana
	# de comandos con permisos y ejecuta el Script.
	
	# Prueba presionando 'Ctrl + Shitf + Esc', con esto deberia
	# abrirse el administrador de tareas.
	# Si no se abre, esta deshabilitado y debes habilitarlo con
	# la opcion "--enable" si lo deseas.
	
	# Tambien lo puedes comprobar presonando 'Ctrl + Alt + Supr'
	# (En ocaciones se llama 'Del' la tecla en lugar de 'Supr'),
	# ahí debe aparecer tambien la opcion de "Administrador de Tareas",
	# si no aparece, habrá que habilitarlo con la opcion "--enable".
	
	# Ver el Modo de Uso Con: python TaskManager.py -h
