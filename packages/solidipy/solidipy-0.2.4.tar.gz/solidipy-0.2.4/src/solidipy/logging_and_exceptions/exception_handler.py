# /utilities/exception/exception_handler.py

""" Exception handler class definition. """

from logging import Logger
from typing import NoReturn, Union

from solidipy.logging_and_exceptions.exception_values import GENERIC_ERROR_DICT, MASTER_EXCEPTION_DICT
from solidipy.logging_and_exceptions.logger import BaseLogger, solidipy_logger as sl


class ExceptionHandler:
	""" Base class for handling exceptions. """

	def __init__(
			self, new_logger: Union[Logger, BaseLogger, None] = None
	):
		"""
		Initializer for the ExceptionHandler class.

		:param new_logger: Instance of a logger class.
		"""
		self.logger = new_logger

	def get_exception_log(self, exception) -> dict:
		"""
		Method for assembling and logging exception information.

		:param exception: Exception object that was raised.
		:return: Formatted dictionary log of exception that occurred.
		"""
		exception_dict: dict = self.__get_exception_dict(
			exception.__class__.__name__
		)

		if self.logger is not None:
			self.__log_exception(exception_dict)
		return exception_dict

	@classmethod
	def __get_exception_dict(cls, exception_key: str) -> dict:
		"""
		Method for retrieving the exception dictionary for a given exception.

		:param exception_key: String name used as a key to retrieve the
			corresponding exception dictionary.
		:return: The requested dictionary of mapped exception values or a
			generic error dictionary if the key is not found.
		"""

		return MASTER_EXCEPTION_DICT.get(exception_key, GENERIC_ERROR_DICT)

	def __log_exception(self, exception_dict: dict) -> NoReturn:
		"""
		Method that formats a log and then logs it.

		:param exception_dict: Exception dictionary to be logged.
		"""

		divider: str = "=" * 100
		log: str = (
			f"\n{divider}\nAn exception occurred:\n{exception_dict}\n{divider}\n"
		)
		self.logger.log_exception(log)  # noqa
		print("\n", log, "\n")


solidipy_exception_handler: ExceptionHandler = ExceptionHandler(sl)
"""
Universal exception handling object for operations across the package.
Not intended for use outside of the package.
"""
