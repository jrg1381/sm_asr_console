import npyscreen
import subprocess
from error_handler import error_handler


class DiagnosticsActionController(npyscreen.ActionControllerSimple):
    def create(self):
        self.add_action(r'^:q', self.quit, False)
    
    def quit(self, command_line, widget_proxy, live):
        self.parent.parentApp.switchFormPrevious()

class DiagnosticsForm(npyscreen.FormMuttActiveTraditionalWithMenus):
    ACTION_CONTROLLER = DiagnosticsActionController

    def __init__(self, *args, **kwargs):
        super(DiagnosticsForm, self).__init__(*args, **kwargs)

    def beforeEditing(self):
        self.root_menu()

    def create(self):
        super().create()
        self.add_handlers({'q': self.parentApp.switchFormPrevious})
        self.wStatus2.value = "CTRL-X to display menu. 'q' to quit. 'l' to search in text."
        self.m1 = self.add_menu(name="Shell commands", shortcut='m')

        commands = (
            'df -k',
            'docker ps',
            'docker ps -a',
            'mount',
            'docker stack ls',
            '/sbin/ifconfig -a',
            'ping -c 5 www.google.com',
            'cat /etc/resolv.conf',
            'traceroute my.nalpeiron.com',
            'docker volume ls',
            'docker volume inspect',
            'docker system prune -f',
            '/sbin/shutdown -h now',
            '/sbin/reboot'
            )

        for c in commands:
            self.m1.addItem(c, self.execute_shell, None, None, (c,))

    @error_handler("Subprocess error")
    def execute_shell(self, *args):
        cmd = args[0].split(' ')
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as cpe:
            output = cpe.output
            raise
        finally:
            self.wMain.values = output.decode('utf-8').split('\n')
