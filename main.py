# Factory Method en Sistema de Notificaciones

from abc import ABC, abstractmethod


# Product
class NotificacionBase(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        pass


# Concrete Products
class NotificacionSMS(NotificacionBase):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando SMS a {destinatario}: {mensaje}")
        # Lógica para enviar SMS
        return True


class NotificacionEmail(NotificacionBase):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando Email a {destinatario}: {mensaje}")
        # Lógica para enviar Email
        return True


class NotificacionPush(NotificacionBase):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando Notificación Push a {destinatario}: {mensaje}")
        # Lógica para enviar Push
        return True


# Creator
class NotificadorBase(ABC):
    @abstractmethod
    def crear_notificacion(self) -> NotificacionBase:
        pass

    def enviar_notificacion(self, mensaje: str, destinatario: str) -> bool:
        notificacion = self.crear_notificacion()
        return notificacion.enviar(mensaje, destinatario)


# Concrete Creators
class NotificadorSMS(NotificadorBase):
    def crear_notificacion(self) -> NotificacionBase:
        return NotificacionSMS()


class NotificadorEmail(NotificadorBase):
    def crear_notificacion(self) -> NotificacionBase:
        return NotificacionEmail()


class NotificadorPush(NotificadorBase):
    def crear_notificacion(self) -> NotificacionBase:
        return NotificacionPush()


# Cliente
def demo_factory_method():
    print("=== Demo Factory Method ===")
    # Uso del patrón Factory Method
    notificadores = [NotificadorSMS(), NotificadorEmail(), NotificadorPush()]
    
    for notificador in notificadores:
        notificador.enviar_notificacion("Nueva actualización disponible", "usuario@ejemplo.com")
    print()


# 2. Singleton - Conexión a Base de Datos

class ConexionBaseDatos:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            print("Creando nueva instancia de conexión a la base de datos")
            cls._instancia = super(ConexionBaseDatos, cls).__new__(cls)
            # Inicializar la conexión
            cls._instancia.conectado = False
        return cls._instancia
    
    def conectar(self):
        if not self.conectado:
            print("Estableciendo conexión a la base de datos...")
            self.conectado = True
        else:
            print("La conexión ya está establecida")
    
    def ejecutar_consulta(self, sql: str):
        if self.conectado:
            print(f"Ejecutando consulta: {sql}")
        else:
            print("Error: No hay conexión establecida")
    
    def cerrar_conexion(self):
        if self.conectado:
            print("Cerrando conexión a la base de datos")
            self.conectado = False
        else:
            print("No hay conexión activa para cerrar")


# Cliente
def demo_singleton():
    print("=== Demo Singleton ===")
    # Intento crear múltiples instancias de la conexión
    conexion1 = ConexionBaseDatos()
    conexion1.conectar()
    conexion1.ejecutar_consulta("SELECT * FROM usuarios")
    
    conexion2 = ConexionBaseDatos()  # Debería devolver la misma instancia
    conexion2.ejecutar_consulta("INSERT INTO productos VALUES (1, 'Producto')")
    
    # Comprobamos si son la misma instancia
    print(f"¿Son la misma instancia? {conexion1 is conexion2}")
    
    conexion1.cerrar_conexion()
    print()


# 3. Abstract Factory - Editor de Documentos Multiplataforma

# Abstract Products
class BotonBase(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def on_click(self):
        pass


class MenuBase(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def seleccionar(self):
        pass


class DialogoBase(ABC):
    @abstractmethod
    def mostrar(self):
        pass
    
    @abstractmethod
    def cerrar(self):
        pass


# Windows Concrete Products
class BotonWindows(BotonBase):
    def render(self):
        print("Renderizando botón estilo Windows")
    
    def on_click(self):
        print("Animación de clic estilo Windows")


class MenuWindows(MenuBase):
    def render(self):
        print("Renderizando menú estilo Windows")
    
    def seleccionar(self):
        print("Selección de menú estilo Windows")


class DialogoWindows(DialogoBase):
    def mostrar(self):
        print("Mostrando diálogo estilo Windows")
    
    def cerrar(self):
        print("Cerrando diálogo estilo Windows")


# MacOS Concrete Products
class BotonMacOS(BotonBase):
    def render(self):
        print("Renderizando botón estilo macOS")
    
    def on_click(self):
        print("Animación de clic estilo macOS")


class MenuMacOS(MenuBase):
    def render(self):
        print("Renderizando menú estilo macOS")
    
    def seleccionar(self):
        print("Selección de menú estilo macOS")


class DialogoMacOS(DialogoBase):
    def mostrar(self):
        print("Mostrando diálogo estilo macOS")
    
    def cerrar(self):
        print("Cerrando diálogo estilo macOS")


# Linux Concrete Products
class BotonLinux(BotonBase):
    def render(self):
        print("Renderizando botón estilo Linux")
    
    def on_click(self):
        print("Animación de clic estilo Linux")


class MenuLinux(MenuBase):
    def render(self):
        print("Renderizando menú estilo Linux")
    
    def seleccionar(self):
        print("Selección de menú estilo Linux")


class DialogoLinux(DialogoBase):
    def mostrar(self):
        print("Mostrando diálogo estilo Linux")
    
    def cerrar(self):
        print("Cerrando diálogo estilo Linux")


# Abstract Factory
class FabricaUIBase(ABC):
    @abstractmethod
    def crear_boton(self) -> BotonBase:
        pass
    
    @abstractmethod
    def crear_menu(self) -> MenuBase:
        pass
    
    @abstractmethod
    def crear_dialogo(self) -> DialogoBase:
        pass


# Concrete Factories
class FabricaUIWindows(FabricaUIBase):
    def crear_boton(self) -> BotonBase:
        return BotonWindows()
    
    def crear_menu(self) -> MenuBase:
        return MenuWindows()
    
    def crear_dialogo(self) -> DialogoBase:
        return DialogoWindows()


class FabricaUIMacOS(FabricaUIBase):
    def crear_boton(self) -> BotonBase:
        return BotonMacOS()
    
    def crear_menu(self) -> MenuBase:
        return MenuMacOS()
    
    def crear_dialogo(self) -> DialogoBase:
        return DialogoMacOS()


class FabricaUILinux(FabricaUIBase):
    def crear_boton(self) -> BotonBase:
        return BotonLinux()
    
    def crear_menu(self) -> MenuBase:
        return MenuLinux()
    
    def crear_dialogo(self) -> DialogoBase:
        return DialogoLinux()


# Editor que usa los componentes
class EditorDocumentos:
    def __init__(self, fabrica_ui: FabricaUIBase):
        self.fabrica_ui = fabrica_ui
        self.boton = fabrica_ui.crear_boton()
        self.menu = fabrica_ui.crear_menu()
        self.dialogo = fabrica_ui.crear_dialogo()
    
    def iniciar(self):
        print("Iniciando Editor de Documentos...")
        self.boton.render()
        self.menu.render()
    
    def abrir_archivo(self):
        self.dialogo.mostrar()
        print("Abriendo archivo...")
        self.dialogo.cerrar()
    
    def guardar_archivo(self):
        self.boton.on_click()
        print("Guardando archivo...")


# Cliente
def demo_abstract_factory():
    print("=== Demo Abstract Factory ===")
    # Crear editor para Windows
    print("Editor en Windows:")
    editor_windows = EditorDocumentos(FabricaUIWindows())
    editor_windows.iniciar()
    editor_windows.abrir_archivo()
    
    print("\nEditor en macOS:")
    editor_macos = EditorDocumentos(FabricaUIMacOS())
    editor_macos.iniciar()
    editor_macos.guardar_archivo()
    
    print("\nEditor en Linux:")
    editor_linux = EditorDocumentos(FabricaUILinux())
    editor_linux.iniciar()
    editor_linux.abrir_archivo()
    editor_linux.guardar_archivo()


# Demo de todos los patrones
if __name__ == "__main__":
    demo_factory_method()
    demo_singleton()
    demo_abstract_factory()