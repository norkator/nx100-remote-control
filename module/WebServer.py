from http.server import HTTPServer, BaseHTTPRequestHandler
from objects import MoveL
from module import Commands, Utils
import os

base_path = os.path.dirname(__file__)


# noinspection PyPep8Naming
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        try:
            if str(self.path) == '/':
                filename = 'index.html'
                html_content = f"<html><body><h1>{message}</h1></body></html>"
                job_name = Commands.read_current_job_details().job_name()
                status = Commands.read_status()
                with open(os.path.join(base_path, filename)) as f:
                    html_content = f.read()
                    html_content = html_content \
                        .replace('{{jobName}}', job_name) \
                        .replace('{{commandRemote}}', str(status.is_command_remote())) \
                        .replace('{{playMode}}', str(status.is_play())) \
                        .replace('{{isHold}}', str(
                        status.is_command_hold() or status.is_command_hold() or status.is_programming_pendant_hold())) \
                        .replace('{{teachMode}}', str(status.is_teach())) \
                        .replace('{{running}}', str(status.is_running())) \
                        .replace('{{servoOn}}', str(status.is_servo_on())) \
                        .replace('{{isError}}', str(status.is_error_occurring()))
                return html_content.encode("utf8")  # NOTE: must return a bytes object!
            else:
                return "".encode('utf-8')
        except Exception as e:
            return html_content.encode("utf8")


    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("Problem with robot connection"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        # print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #       str(self.path), str(self.headers), post_data.decode('utf-8'))
        command = post_data.decode("utf-8")
        if command == 'start_job':
            Commands.write_start_job('')
        elif command == 'hold_on':
            Commands.write_hold('1')
        elif command == 'hold_off':
            Commands.write_hold('0')
        elif command == 'servo_on':
            Commands.write_servo_power('1')
        elif command == 'servo_off':
            Commands.write_servo_power('0')
        elif command == 'move_s_l':
            c_pos = Commands.read_current_specified_coordinate_system_position('0', '0')
            Commands.write_linear_move(MoveL.MoveL(
                0, 20, 0,
                (c_pos.get_x() - 10), c_pos.get_y(), c_pos.get_z(), c_pos.get_tx(), c_pos.get_ty(), c_pos.get_tz(),
                Utils.binary_to_decimal(0x00000001)
            ))
        elif command == 'move_s_r':
            c_pos = Commands.read_current_specified_coordinate_system_position('0', '0')
            Commands.write_linear_move(MoveL.MoveL(
                0, 20, 0,
                (c_pos.get_x() + 10), c_pos.get_y(), c_pos.get_z(), c_pos.get_tx(), c_pos.get_ty(), c_pos.get_tz(),
                Utils.binary_to_decimal(0x00000001)
            ))

        self._set_headers()
        self.wfile.write("".format(self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8080):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()
