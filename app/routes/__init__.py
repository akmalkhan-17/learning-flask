from .auth import (
    auth_bp,
)  # now the import in create_app() function is not needed as we have already imported it here and registered the blueprint in the create_app() function
