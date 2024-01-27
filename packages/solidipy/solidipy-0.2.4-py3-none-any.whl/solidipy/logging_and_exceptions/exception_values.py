# utilities/exception/exception_values.py

"""
Module of Error constants used in the exception handler.
Exceptions are listed in order of inheritance.
"""

from binascii import Error as BinasciiError, Incomplete as BinasciiIncompleteError
from importlib.util import find_spec
from json import JSONDecodeError
from typing import Optional

SA_EXCEPTION_TUPLE: Optional[tuple] = None
SQLALCHEMY_AVAILABLE: bool = find_spec("sqlalchemy") is not None
if SQLALCHEMY_AVAILABLE:
	from sqlalchemy.exc import (  # noqa
		AmbiguousForeignKeysError,  # noqa
		ArgumentError,  # noqa
		CircularDependencyError,  # noqa
		CompileError,  # noqa
		DBAPIError,  # noqa
		DataError,  # noqa
		DatabaseError,  # noqa
		DisconnectionError,  # noqa
		IdentifierError,  # noqa
		IntegrityError,  # noqa
		InterfaceError,  # noqa
		InternalError,  # noqa
		InvalidRequestError,  # noqa
		InvalidatePoolError,  # noqa
		MultipleResultsFound,  # noqa
		NoForeignKeysError,  # noqa
		NoInspectionAvailable,  # noqa
		NoReferenceError,  # noqa
		NoReferencedColumnError,  # noqa
		NoReferencedTableError,  # noqa
		NoResultFound,  # noqa
		NoSuchColumnError,  # noqa
		NoSuchModuleError,  # noqa
		NoSuchTableError,  # noqa
		NotSupportedError,  # noqa
		ObjectNotExecutableError,  # noqa
		OperationalError,  # noqa
		PendingRollbackError,  # noqa
		ProgrammingError,  # noqa
		ResourceClosedError,  # noqa
		SADeprecationWarning,  # noqa
		SAPendingDeprecationWarning,  # noqa
		SAWarning,  # noqa
		SQLAlchemyError,  # noqa
		StatementError,  # noqa
		UnboundExecutionError,  # noqa
		UnreflectableTableError,  # noqa
		UnsupportedCompilationError,  # noqa
	)

# -----------------------------------------------------------------------
# ------------------------ Begin error messages -------------------------
# -----------------------------------------------------------------------

# ------------------ Generic' error message constants -------------------
GENERIC_MESSAGE_KEY: str = "Message"
GENERIC_CODE_KEY: str = "Code"
GENERIC_ERROR_NAME_VALUE: str = "Generic error"
GENERIC_ERROR_MESSAGE_VALUE: str = "An error outside of the scope of the error handler has occurred."

# ------------------ 'SQLAlchemy' error message constants ---------------
NO_SUCH_MODULE_ERROR_MESSAGE: str = "A dynamically-loaded database module of a particular name cannot be located."
OBJECT_NOT_EXECUTABLE_ERROR_MESSAGE: str = "An object was passed to .execute() that can't be executed as SQL."
NO_FOREIGN_KEYS_ERROR_MESSAGE: str = "During a join, no foreign keys could be located between two selectables."
AMBIGUOUS_FOREIGN_KEYS_ERROR_MESSAGE: str = "During a join, more than one matching foreign key was located between two selectables."
ARGUMENT_ERROR_MESSAGE: str = "Invalid or conflicting function argument was supplied."
CIRCULAR_DEPENDENCY_ERROR_MESSAGE: str = "Topological sorts detected a circular dependency."
UNSUPPORTED_COMPILATION_ERROR_MESSAGE: str = "Operation is not supported by the given compiler."
COMPILE_ERROR_MESSAGE: str = "An error occurred during SQL compilation."
IDENTIFIER_ERROR_MESSAGE: str = "Schema name is beyond the max character limit."
INVALIDATE_POOL_ERROR_MESSAGE: str = "The connection pool should invalidate all stale connections."
DISCONNECTION_ERROR_MESSAGE: str = "A disconnect was detected on a raw DB-API connection."
NO_INSPECTION_AVAILABLE_ERROR_MESSAGE: str = "Subject produced no context for inspection."
PENDING_ROLLBACK_ERROR_MESSAGE: str = "A transaction has failed and needs to be rolled back before; continuing."
RESOURCE_CLOSED_ERROR_MESSAGE: str = "An operation was requested from a connection, cursor, or other object that's in a closed state."
NO_SUCH_COLUMN_ERROR_MESSAGE: str = "A nonexistent column was requested from a `Row `."
NO_RESULT_FOUND_ERROR_MESSAGE: str = "A database result was required, but none was found."
MULTIPLE_RESULTS_FOUND_ERROR_MESSAGE: str = "A single database result was required, but more than one were found."
NO_REFERENCED_TABLE_ERROR_MESSAGE: str = "`Foreign Key` references a `Table` that cannot be located."
NO_REFERENCED_COLUMN_ERROR_MESSAGE: str = "`Foreign Key` references a `Column` that cannot be located."
NO_REFERENCE_ERROR_MESSAGE: str = "`Foreign Key` references an unresolved attribute."
NO_SUCH_TABLE_ERROR_MESSAGE: str = "`Table` does not exist or is not visible to a connection."
UNREFLECTABLE_TABLE_ERROR_MESSAGE: str = "`Table` exists but can't be reflected."
UNBOUND_EXECUTION_ERROR_MESSAGE: str = "SQL execution was attempted without a database connection to execute it on."
INVALID_REQUEST_ERROR_MESSAGE: str = "SQLAlchemy was asked to do something it can't do."
INTERFACE_ERROR_MESSAGE: str = "A DB-API InterfaceError occurred."
DATA_ERROR_MESSAGE: str = "There was a problem with the data received from the DB-API"
STATEMENT_ERROR_MESSAGE: str = "An error occurred during execution of a SQL statement."
SQLALCHEMY_ERROR_MESSAGE: str = "A generic error occurred in SQLAlchemy."
OPERATIONAL_ERROR_MESSAGE: str = "There was an operational error between SQLAlchemy and the DB-API"
INTEGRITY_ERROR_MESSAGE: str = "The Integrity of the connection between SQLAlchemy and the DB-API was compromised."
INTERNAL_ERROR_MESSAGE: str = "An internal error occurred between SQLAlchemy and the DB-API."
PROGRAMMING_ERROR_MESSAGE: str = "A programming error occurred between SQLAlchemy and the DB-API."
NOT_SUPPORTED_ERROR_MESSAGE: str = "SQLAlchemy attempted to use an unsupported function of the DB-API."
DATABASE_ERROR_MESSAGE: str = "The DB-API has raised a DatabaseError."
DBAPI_ERROR_MESSAGE: str = "An error occurred in the DB-API."
SA_WARNING_MESSAGE: str = "Dubious SQLAlchemy runtime error detected."
SA_PENDING_DEPRECATION_WARNING_MESSAGE: str = "SQLAlchemy features in use that will soon be marked as deprecated."
SA_DEPRECATION_WARNING_MESSAGE: str = "SQLAlchemy features in use that have been marked as deprecated."

# ------------- 'Unicode' error message constants ------------------------
UNICODE_TRANSL_ERROR_MESSAGE: str = "A unicode error occurred during translation."
UNICODE_ENCODE_ERROR_MESSAGE: str = "An error occurred related to unicode encoding."
UNICODE_DECODE_ERROR_MESSAGE: str = "An error occurred related to unicode decoding."
UNICODE_ERROR_MESSAGE: str = "An error occurred related to unicode encoding or decoding."
BINASCII_ERROR_MESSAGE: str = "An error occurred related to binary encoding or decoding."
JSON_DECODE_ERROR_MESSAGE: str = "Data could not be decoded as valid JSON."

# ----------------- 'Standard' error message constants -------------------
VALUE_ERROR_MESSAGE: str = "An operation or function received an argument that has the right type but an inappropriate value. The situation is not an IndexError."
TYPE_ERROR_MESSAGE: str = "An error occurred due to type mismatch."
SYSTEM_ERROR_MESSAGE: str = "The interpreter found a non-critical internal error. This should be reported to the author or maintainer of your Python interpreter."
TAB_ERROR_MESSAGE: str = "Incorrect use of Tabs and Spaces."
INDENTATION_ERROR_MESSAGE: str = "Incorrect indentation detected."
SYNTAX_ERROR_MESSAGE: str = "Syntax error encountered."
STOP_ITERATION_ERROR_MESSAGE: str = "The iterator has no more items to return."
STOP_ASYNC_ITERATION_MESSAGE: str = "The asynchronous iterator has no more items to return."
RECURSION_ERROR_MESSAGE: str = "Maximum recursion depth has been exceeded."
NOT_IMPLEMENTED_ERROR_MESSAGE: str = "This method or function should be implemented in the derived class."
RUN_TIME_ERROR_MESSAGE: str = "An error has been detected at runtime that does not fall in any of the other categories."
REFERENCE_ERROR_MESSAGE: str = "Attempt to access a deleted reference."

# ------------------- 'os' error message constants -----------------------
TIMEOUT_ERROR_MESSAGE: str = "A system function timed out at the system level."
PROCESS_LOOKUP_ERROR_MESSAGE: str = "Failed to find the given process."
PERMISSION_ERROR_MESSAGE: str = "An operation was not permitted."
NOT_A_DIRECTORY_ERROR_MESSAGE: str = "Expected a directory but got something else."
IS_A_DIRECTORY_ERROR_MESSAGE: str = "Expected something other than a directory but got a directory."
INTERRUPTED_ERROR_MESSAGE: str = "A system call has been interrupted by an incoming signal."
FILE_NOT_FOUND_ERROR_MESSAGE: str = "The specified file was not found."
FILE_EXISTS_ERROR_MESSAGE: str = "The file already exists."
CONNECTION_RESET_ERROR_MESSAGE: str = "Connection has been reset by the peer."
CONNECTION_REFUSED_ERROR_MESSAGE: str = "Connection has been refused by the peer."
CONNECTION_ABORTED_ERROR_MESSAGE: str = "Connection has been aborted by the peer."
BROKEN_PIPE_ERROR_MESSAGE: str = "Tried to write on a pipe while the other end was closed or tried to write on a socket that was shutdown for writing."
CONNECTION_ERROR_MESSAGE: str = "An unknown connection-related issue occurred."
CHILD_PROCESS_ERROR_MESSAGE: str = "An operation on a child process has failed."
BLOCKING_IO_ERROR_MESSAGE: str = "An operation would have blocked on an object that has non-blocking operation enabled."

# -------------- 'Standard' error message constants (Cont.) --------------
OS_ERROR_MESSAGE: str = "A system function has returned a system-related error, this could include I/O failures such as “file not found” or “disk full” (not for illegal argument types or other incidental errors)."
UNBOUND_LOCAL_ERROR_MESSAGE: str = "Referenced a local variable before it was defined."
NAME_ERROR_MESSAGE: str = "A local or global name was not found. This applies only to unqualified names."
MEMORY_ERROR_MESSAGE: str = "An operation has run out of memory but the situation may still be rescued by deleting some objects."
KEY_ERROR_MESSAGE: str = "Mapping (dictionary) key not found in the set of existing keys."
INDEX_ERROR_MESSAGE: str = "Sequence subscript is out of range."
LOOKUP_ERROR_MESSAGE: str = "A key or index used on a mapping or sequence is invalid: IndexError or KeyError."
MODULE_NOT_FOUND_ERROR_MESSAGE: str = "The specified module could not be found."
IMPORT_ERROR_MESSAGE: str = "Failed to import a module or its part."
EOF_ERROR_MESSAGE: str = "End of file reached without reading any data."
BUFFER_ERROR_MESSAGE: str = "A buffer-related operation cannot be performed."
ATTRIBUTE_ERROR_MESSAGE: str = "An attribute reference or assignment has failed."
ASSERTION_ERROR_MESSAGE: str = "Assertion failed."
ZERO_DIVISION_ERROR_MESSAGE: str = "The second argument of a division or modulo operation is zero."
OVERFLOW_ERROR_MESSAGE: str = "Result of an arithmetic operation is too large to be represented."
FLOATING_POINT_ERROR_MESSAGE: str = "Floating point operation has failed."
ARITHMETIC_ERROR_MESSAGE: str = "An arithmetic error has occurred. OverflowError, ZeroDivisionError, or FloatingPointError."
BINASCII_INCOMPLETE_ERROR_MESSAGE: str = "Incomplete input data."
BASE_EXCEPTION_ERROR_MESSAGE: str = "A system-exiting exception has occurred."
EXCEPTION_ERROR_MESSAGE: str = "A non-system-exiting exception has occurred."
GENERATOR_EXIT_ERROR_MESSAGE: str = "Operation was performed on an active generator that was already closed."
BASE_EXCEPTION_GROUP_ERROR_MESSAGE: str = "Multiple simultaneous exceptions were grouped together."

# ------------------------------------------------------------------------
# -------------------------- Begin error codes ---------------------------
# ------------------------------------------------------------------------

# -------------------- 'Generic' error code constants --------------------
GENERIC_ERROR_CODE: str = "GENERIC ERROR CODE"

# ------------------ 'SQLAlchemy' error code constants -------------------
UNSUPPORTED_COMPILATION_ERROR_CODE: str = "l7de"
SQLALCHEMY_ERROR_CODE: str = "code"
INTERFACE_ERROR_CODE: str = "rvf5"
DATABASE_ERROR_CODE: str = "4xp6"
DATA_ERROR_CODE: str = "9h9h"
OPERATIONAL_ERROR_CODE: str = "e3q8"
INTEGRITY_ERROR_CODE: str = "gkpj"
INTERNAL_ERROR_CODE: str = "2j85"
PROGRAMMING_ERROR_CODE: str = "f405"
NOT_SUPPORTED_ERROR_CODE: str = "tw8g"
DB_API_ERROR_CODE: str = "dbapi"

# --------------------'os' error code constants --------------------------
TIMEOUT_ERROR_CODE: str = "errno ETIMEDOUT"
INTERRUPTED_ERROR_CODE: str = "errno EINTR"
CONNECTION_RESET_ERROR_CODE: str = "errno ECONNRESET"
CONNECTION_REFUSED_ERROR_CODE: str = "errno ECONNRESET"
CONNECTION_ABORTED_ERROR_CODE: str = "errno ECONNABORTED"
BROKEN_PIPE_ERROR_CODE: str = "errno EPIPE, errno ESHUTDOWN"
CHILD_PROCESS_ERROR_CODE: str = "errno ECHILD"
BLOCKING_IO_CODE: str = "errno EAGAIN, errno EALREADY, errno EWOULDBLOCK, errno EINPROGRESS"
PERMISSION_ERROR_CODE: str = "errno EACCES, EPERM"

# -----------------------------------------------------------------------
# ------------------- Begin Exception Values -----------------------
# ------------------------------------------------------------------------

# -----------------------------------------------------------------------
# ------------------- Begin Exception dictionaries -----------------------
# ------------------------------------------------------------------------

# --------------------- 'Generic' error dictionaries ---------------------
GENERIC_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: GENERIC_ERROR_MESSAGE_VALUE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}

# ------------------- 'SQLAlchemy' error dictionaries --------------------
OBJECT_NOT_EXECUTABLE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: OBJECT_NOT_EXECUTABLE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_SUCH_MODULE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_SUCH_MODULE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_FOREIGN_KEYS_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_FOREIGN_KEYS_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
AMBIGUOUS_FOREIGN_KEYS_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: AMBIGUOUS_FOREIGN_KEYS_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
ARGUMENT_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: ARGUMENT_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
CIRCULAR_DEPENDENCY_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: CIRCULAR_DEPENDENCY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
UNSUPPORTED_COMPILATION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNSUPPORTED_COMPILATION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: UNSUPPORTED_COMPILATION_ERROR_CODE
}
COMPILE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: COMPILE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
IDENTIFIER_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: IDENTIFIER_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
INVALIDATE_POOL_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INVALIDATE_POOL_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
DISCONNECTION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: DISCONNECTION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_INSPECTION_AVAILABLE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_INSPECTION_AVAILABLE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
PENDING_ROLLBACK_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: PENDING_ROLLBACK_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
RESOURCE_CLOSED_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: RESOURCE_CLOSED_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_SUCH_COLUMN_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_SUCH_COLUMN_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_RESULT_FOUND_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_RESULT_FOUND_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
MULTIPLE_RESULTS_FOUND_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: MULTIPLE_RESULTS_FOUND_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_REFERENCED_TABLE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_REFERENCED_TABLE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_REFERENCED_COLUMN_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_REFERENCED_COLUMN_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_REFERENCE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_REFERENCE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
NO_SUCH_TABLE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NO_SUCH_TABLE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
UNREFLECTABLE_TABLE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNREFLECTABLE_TABLE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
UNBOUND_EXECUTION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNBOUND_EXECUTION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
INVALID_REQUEST_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INVALID_REQUEST_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
INTERFACE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INTERFACE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: INTERFACE_ERROR_CODE
}
DATA_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: DATA_ERROR_MESSAGE,
	GENERIC_CODE_KEY: DATA_ERROR_CODE
}
STATEMENT_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: STATEMENT_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
SQLALCHEMY_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: SQLALCHEMY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE
}
OPERATIONAL_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: OPERATIONAL_ERROR_MESSAGE,
	GENERIC_CODE_KEY: OPERATIONAL_ERROR_CODE
}
INTEGRITY_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INTEGRITY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: INTEGRITY_ERROR_CODE
}
INTERNAL_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INTERNAL_ERROR_MESSAGE,
	GENERIC_CODE_KEY: INTERNAL_ERROR_CODE
}
PROGRAMMING_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: PROGRAMMING_ERROR_MESSAGE,
	GENERIC_CODE_KEY: PROGRAMMING_ERROR_CODE
}
NOT_SUPPORTED_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NOT_SUPPORTED_ERROR_MESSAGE,
	GENERIC_CODE_KEY: NOT_SUPPORTED_ERROR_CODE
}
DATABASE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: DATABASE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: DB_API_ERROR_CODE
}
DBAPI_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: DBAPI_ERROR_MESSAGE,
	GENERIC_CODE_KEY: DB_API_ERROR_CODE
}
SA_DEPRECATION_WARNING_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: SA_DEPRECATION_WARNING_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
SA_PENDING_DEPRECATION_WARNING_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: SA_PENDING_DEPRECATION_WARNING_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
SA_WARNING_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: SA_WARNING_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}

# --------------------- 'unicode' error dictionaries ---------------------
UNICODE_TRANSL_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNICODE_TRANSL_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
UNICODE_ENCODE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNICODE_ENCODE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
UNICODE_DECODE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNICODE_DECODE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
UNICODE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNICODE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
BINASCII_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: BINASCII_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
JSON_DECODE_DICT: dict = {
	GENERIC_MESSAGE_KEY: JSON_DECODE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}

# -------------------- 'Standard' error dictionaries ---------------------
VALUE_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: VALUE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
TYPE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: TYPE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
SYSTEM_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: SYSTEM_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
TAB_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: TAB_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
INDENTATION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INDENTATION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
SYNTAX_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: SYNTAX_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
STOP_ITERATION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: STOP_ITERATION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
STOP_ASYNC_ITERATION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: STOP_ASYNC_ITERATION_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
RECURSION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: RECURSION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
NOT_IMPLEMENTED_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NOT_IMPLEMENTED_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
RUN_TIME_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: RUN_TIME_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
REFERENCE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: REFERENCE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
TIMEOUT_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: TIMEOUT_ERROR_MESSAGE,
	GENERIC_CODE_KEY: TIMEOUT_ERROR_CODE,
}
PROCESS_LOOKUP_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: PROCESS_LOOKUP_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
PERMISSION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: PERMISSION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: PERMISSION_ERROR_CODE,
}
NOT_A_DIRECTORY_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NOT_A_DIRECTORY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
IS_A_DIRECTORY_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: IS_A_DIRECTORY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
INTERRUPTED_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INTERRUPTED_ERROR_MESSAGE,
	GENERIC_CODE_KEY: INTERRUPTED_ERROR_CODE,
}
FILE_NOT_FOUND_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: FILE_NOT_FOUND_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
FILE_EXISTS_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: FILE_EXISTS_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
CONNECTION_RESET_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: CONNECTION_RESET_ERROR_MESSAGE,
	GENERIC_CODE_KEY: CONNECTION_RESET_ERROR_CODE,
}
CONNECTION_REFUSED_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: CONNECTION_REFUSED_ERROR_MESSAGE,
	GENERIC_CODE_KEY: CONNECTION_REFUSED_ERROR_CODE,
}
CONNECTION_ABORTED_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: CONNECTION_ABORTED_ERROR_MESSAGE,
	GENERIC_CODE_KEY: CONNECTION_ABORTED_ERROR_CODE,
}
BROKEN_PIPE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: BROKEN_PIPE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: BROKEN_PIPE_ERROR_CODE,
}
CONNECTION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: CONNECTION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
CHILD_PROCESS_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: CHILD_PROCESS_ERROR_MESSAGE,
	GENERIC_CODE_KEY: CHILD_PROCESS_ERROR_CODE,
}
BLOCKING_IO_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: BLOCKING_IO_ERROR_MESSAGE,
	GENERIC_CODE_KEY: BLOCKING_IO_CODE,
}
OS_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: OS_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
UNBOUND_LOCAL_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: UNBOUND_LOCAL_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
NAME_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: NAME_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
MEMORY_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: MEMORY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
KEY_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: KEY_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
INDEX_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: INDEX_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
LOOKUP_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: LOOKUP_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
MODULE_NOT_FOUND_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: MODULE_NOT_FOUND_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
IMPORT_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: IMPORT_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
END_OF_FILE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: EOF_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
BUFFER_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: BUFFER_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
ATTRIBUTE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: ATTRIBUTE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
ASSERTION_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: ASSERTION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
ZERO_DIVISION_ERROR_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: ZERO_DIVISION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
OVERFLOW_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: OVERFLOW_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
FLOATING_POINT_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: FLOATING_POINT_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
ARITHMETIC_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: ARITHMETIC_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
BINASCII_INCOMPLETE_ERROR_DICT: dict = {
	GENERIC_MESSAGE_KEY: BINASCII_INCOMPLETE_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
BASE_EXCEPTION_DICT: dict = {
	GENERIC_MESSAGE_KEY: BASE_EXCEPTION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
EXCEPTION_DICT: dict = {
	GENERIC_MESSAGE_KEY: EXCEPTION_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
GENERATOR_EXIT_DICT: dict = {
	GENERIC_MESSAGE_KEY: GENERATOR_EXIT_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}
BASE_EXCEPTION_GROUP_DICT: dict = {
	GENERIC_MESSAGE_KEY: BASE_EXCEPTION_GROUP_ERROR_MESSAGE,
	GENERIC_CODE_KEY: GENERIC_ERROR_CODE,
}

# -------------------- 'Master' error dictionary ---------------------
MASTER_EXCEPTION_DICT: dict = {
	UnicodeTranslateError.__name__: UNICODE_TRANSL_ERROR_DICT,
	UnicodeEncodeError.__name__: UNICODE_ENCODE_ERROR_DICT,
	UnicodeDecodeError.__name__: UNICODE_DECODE_ERROR_DICT,
	UnicodeError.__name__: UNICODE_ERROR_DICT,
	BinasciiError.__name__: BINASCII_ERROR_DICT,
	JSONDecodeError.__name__: JSON_DECODE_DICT,
	ValueError.__name__: VALUE_ERROR_ERROR_DICT,
	TypeError.__name__: TYPE_ERROR_DICT,
	SystemError.__name__: SYSTEM_ERROR_ERROR_DICT,
	TabError.__name__: TAB_ERROR_DICT,
	IndentationError.__name__: INDENTATION_ERROR_DICT,
	SyntaxError.__name__: SYNTAX_ERROR_DICT,
	StopIteration.__name__: STOP_ITERATION_ERROR_DICT,
	StopAsyncIteration.__name__: STOP_ASYNC_ITERATION_ERROR_DICT,
	RecursionError.__name__: RECURSION_ERROR_DICT,
	NotImplementedError.__name__: NOT_IMPLEMENTED_ERROR_DICT,
	RuntimeError.__name__: RUN_TIME_ERROR_ERROR_DICT,
	ReferenceError.__name__: REFERENCE_ERROR_DICT,
	TimeoutError.__name__: TIMEOUT_ERROR_DICT,
	ProcessLookupError.__name__: PROCESS_LOOKUP_ERROR_DICT,
	PermissionError.__name__: PERMISSION_ERROR_DICT,
	NotADirectoryError.__name__: NOT_A_DIRECTORY_ERROR_DICT,
	IsADirectoryError.__name__: IS_A_DIRECTORY_ERROR_DICT,
	InterruptedError.__name__: INTERRUPTED_ERROR_DICT,
	FileNotFoundError.__name__: FILE_NOT_FOUND_ERROR_DICT,
	FileExistsError.__name__: FILE_EXISTS_ERROR_DICT,
	ConnectionResetError.__name__: CONNECTION_RESET_ERROR_DICT,
	ConnectionRefusedError.__name__: CONNECTION_REFUSED_ERROR_DICT,
	ConnectionAbortedError.__name__: CONNECTION_ABORTED_ERROR_DICT,
	BrokenPipeError.__name__: BROKEN_PIPE_ERROR_DICT,
	ConnectionError.__name__: CONNECTION_ERROR_DICT,
	ChildProcessError.__name__: CHILD_PROCESS_ERROR_DICT,
	BlockingIOError.__name__: BLOCKING_IO_ERROR_DICT,
	OSError.__name__: OS_ERROR_ERROR_DICT,
	UnboundLocalError.__name__: UNBOUND_LOCAL_ERROR_DICT,
	NameError.__name__: NAME_ERROR_ERROR_DICT,
	MemoryError.__name__: MEMORY_ERROR_ERROR_DICT,
	KeyError.__name__: KEY_ERROR_DICT,
	IndexError.__name__: INDEX_ERROR_ERROR_DICT,
	LookupError.__name__: LOOKUP_ERROR_ERROR_DICT,
	ModuleNotFoundError.__name__: MODULE_NOT_FOUND_ERROR_DICT,
	ImportError.__name__: IMPORT_ERROR_DICT,
	EOFError.__name__: END_OF_FILE_ERROR_DICT,
	BufferError.__name__: BUFFER_ERROR_DICT,
	AttributeError.__name__: ATTRIBUTE_ERROR_DICT,
	AssertionError.__name__: ASSERTION_ERROR_DICT,
	ZeroDivisionError.__name__: ZERO_DIVISION_ERROR_ERROR_DICT,
	OverflowError.__name__: OVERFLOW_ERROR_DICT,
	FloatingPointError.__name__: FLOATING_POINT_ERROR_DICT,
	ArithmeticError.__name__: ARITHMETIC_ERROR_DICT,
	BinasciiIncompleteError.__name__: BINASCII_INCOMPLETE_ERROR_DICT,
	Exception.__name__: EXCEPTION_DICT,
	GeneratorExit.__name__: GENERATOR_EXIT_DICT,
	BaseException.__name__: BASE_EXCEPTION_DICT,
}
if SQLALCHEMY_AVAILABLE:
	MASTER_EXCEPTION_DICT.update(
		{
			ObjectNotExecutableError.__name__: OBJECT_NOT_EXECUTABLE_ERROR_DICT,
			NoSuchModuleError.__name__: NO_SUCH_MODULE_ERROR_DICT,
			NoForeignKeysError.__name__: NO_FOREIGN_KEYS_ERROR_DICT,
			AmbiguousForeignKeysError.__name__: AMBIGUOUS_FOREIGN_KEYS_ERROR_DICT,
			ArgumentError.__name__: ARGUMENT_ERROR_DICT,
			CircularDependencyError.__name__: CIRCULAR_DEPENDENCY_ERROR_DICT,
			UnsupportedCompilationError.__name__: UNSUPPORTED_COMPILATION_ERROR_DICT,
			CompileError.__name__: COMPILE_ERROR_DICT,
			IdentifierError.__name__: IDENTIFIER_ERROR_DICT,
			InvalidatePoolError.__name__: INVALIDATE_POOL_ERROR_DICT,
			DisconnectionError.__name__: DISCONNECTION_ERROR_DICT,
			NoInspectionAvailable.__name__: NO_INSPECTION_AVAILABLE_ERROR_DICT,
			PendingRollbackError.__name__: PENDING_ROLLBACK_ERROR_DICT,
			ResourceClosedError.__name__: RESOURCE_CLOSED_ERROR_DICT,
			NoSuchColumnError.__name__: NO_SUCH_COLUMN_ERROR_DICT,
			NoResultFound.__name__: NO_RESULT_FOUND_ERROR_DICT,
			MultipleResultsFound.__name__: MULTIPLE_RESULTS_FOUND_ERROR_DICT,
			NoReferencedTableError.__name__: NO_REFERENCED_TABLE_ERROR_DICT,
			NoReferencedColumnError.__name__: NO_REFERENCED_COLUMN_ERROR_DICT,
			NoReferenceError.__name__: NO_REFERENCE_ERROR_DICT,
			NoSuchTableError.__name__: NO_SUCH_TABLE_ERROR_DICT,
			UnreflectableTableError.__name__: UNREFLECTABLE_TABLE_ERROR_DICT,
			UnboundExecutionError.__name__: UNBOUND_EXECUTION_ERROR_DICT,
			InvalidRequestError.__name__: INVALID_REQUEST_ERROR_DICT,
			InterfaceError.__name__: INTERFACE_ERROR_DICT,
			DataError.__name__: DATA_ERROR_DICT,
			StatementError.__name__: STATEMENT_ERROR_DICT,
			SQLAlchemyError.__name__: SQLALCHEMY_ERROR_DICT,
			OperationalError.__name__: OPERATIONAL_ERROR_DICT,
			IntegrityError.__name__: INTEGRITY_ERROR_DICT,
			InternalError.__name__: INTERNAL_ERROR_DICT,
			ProgrammingError.__name__: PROGRAMMING_ERROR_DICT,
			NotSupportedError.__name__: NOT_SUPPORTED_ERROR_DICT,
			DatabaseError.__name__: DATABASE_ERROR_DICT,
			DBAPIError.__name__: DBAPI_ERROR_DICT,
			SADeprecationWarning.__name__: SA_DEPRECATION_WARNING_ERROR_DICT,
			SAPendingDeprecationWarning.__name__: SA_PENDING_DEPRECATION_WARNING_ERROR_DICT,
			SAWarning.__name__: SA_WARNING_ERROR_DICT,
		}
	)
"""
Main mapping dict that holds exceptions and their associated error sub dicts.
Exceptions are listed in order of inheritance.
"""

EXCEPTION_TUPLE: tuple = (
	UnicodeTranslateError,
	UnicodeEncodeError,
	UnicodeDecodeError,
	UnicodeError,
	BinasciiError,
	JSONDecodeError,
	ValueError,
	TypeError,
	SystemError,
	TabError,
	IndentationError,
	SyntaxError,
	StopIteration,
	StopAsyncIteration,
	RecursionError,
	NotImplementedError,
	RuntimeError,
	ReferenceError,
	TimeoutError,
	ProcessLookupError,
	PermissionError,
	NotADirectoryError,
	IsADirectoryError,
	InterruptedError,
	FileNotFoundError,
	FileExistsError,
	ConnectionResetError,
	ConnectionRefusedError,
	ConnectionAbortedError,
	BrokenPipeError,
	ConnectionError,
	ChildProcessError,
	BlockingIOError,
	OSError,
	UnboundLocalError,
	NameError,
	MemoryError,
	KeyError,
	IndexError,
	LookupError,
	ModuleNotFoundError,
	ImportError,
	EOFError,
	BufferError,
	AttributeError,
	AssertionError,
	ZeroDivisionError,
	OverflowError,
	FloatingPointError,
	ArithmeticError,
	BinasciiIncompleteError,
	Exception,
	GeneratorExit,
	BaseException
)
"""
Tuple of exceptions listed in order of inheritance
with child classes being listed first.
"""

MASTER_EXCEPTION_TUPLE: tuple = EXCEPTION_TUPLE
"""
Tuple of all exceptions listed in order of inheritance
with child classes being listed first.
"""

if SQLALCHEMY_AVAILABLE:
	SA_EXCEPTION_TUPLE: tuple = (
		ObjectNotExecutableError,
		NoSuchModuleError,
		NoForeignKeysError,
		AmbiguousForeignKeysError,
		ArgumentError,
		CircularDependencyError,
		UnsupportedCompilationError,
		CompileError,
		IdentifierError,
		InvalidatePoolError,
		DisconnectionError,
		NoInspectionAvailable,
		PendingRollbackError,
		ResourceClosedError,
		NoSuchColumnError,
		NoResultFound,
		MultipleResultsFound,
		NoReferencedTableError,
		NoReferencedColumnError,
		NoReferenceError,
		NoSuchTableError,
		UnreflectableTableError,
		UnboundExecutionError,
		InvalidRequestError,
		InterfaceError,
		DataError,
		StatementError,
		SQLAlchemyError,
		OperationalError,
		IntegrityError,
		InternalError,
		ProgrammingError,
		NotSupportedError,
		DatabaseError,
		DBAPIError,
		SADeprecationWarning,
		SAPendingDeprecationWarning,
		SAWarning,
	)
	"""
	Tuple of SQLAlchemy exceptions listed in order of inheritance
	with child classes being listed first.
	"""
	MASTER_EXCEPTION_TUPLE = (EXCEPTION_TUPLE + SA_EXCEPTION_TUPLE)
