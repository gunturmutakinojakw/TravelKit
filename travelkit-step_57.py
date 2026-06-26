# === Stage 57: Add structured result objects for command handlers ===
# Project: TravelKit
class CommandResult(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None


def create_success_result(data: Any, message: str = "Operation completed") -> CommandResult:
    return CommandResult(success=True, message=message, data=data)


def create_error_result(error_msg: str, details: Optional[dict] = None) -> CommandResult:
    return CommandResult(
        success=False, 
        message=error_msg, 
        error=str(details.get("message", error_msg)) if details else error_msg
    )
