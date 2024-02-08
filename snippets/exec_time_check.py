from datetime import datetime
r = datetime.now().timestamp()
exec(args[0])
r = datetime.now().timestamp() - r