# encoding: utf-8
import npyscreen
from error_handler import error_handler,DialogType
from swagger_client.models import ManagementMaxWorkers

API_ERROR_TEXT="API error (management_api)"

class EditWorkers(npyscreen.ActionFormV2):
    @error_handler(title=API_ERROR_TEXT)
    def _fetch_max_workers(self):
        response = self.management_api.get_max_workers()
        return response.count

    @error_handler(title=API_ERROR_TEXT)
    def _modify_worker_count_unchecked(self, value):
        request = ManagementMaxWorkers(count=value)
        response = self.management_api.set_max_workers(request)
        return response.count == value

    def _modify_worker_count(self):
        try:
            value = int(self.wg_max_workers.value)
            if value < 0:
                raise ValueError
        except ValueError:
            npyscreen.notify_wait("{} is not a number >= 0".format(self.wg_max_workers.value))
            return False

        return self._modify_worker_count_unchecked(value)

    def create(self):
        self.management_api = self.parentApp.management_api
        self.wg_max_workers = self.add(npyscreen.TitleText, width=80, name="Max workers")
    
    def on_ok(self):
        if self._modify_worker_count():
            self.parentApp.switchFormPrevious()

    def beforeEditing(self):
        self.wg_max_workers.value = self._fetch_max_workers() or "??"

    def on_cancel(self):
        self.parentApp.switchFormPrevious()