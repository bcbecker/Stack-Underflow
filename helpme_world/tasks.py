from rq import get_current_job
from helpme_world import create_app, db
from helpme_world.models import User, Task
from helpme_world.users.utils import save_picture, send_reset_email


app = create_app()
app.app_context().push()


def _set_task_progress(progress):
    """
    Util to set the task progress as it executes
    """
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        task.user.add_notification('task_progress', {'task_id': job.get_id(),
                                                     'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()


def send_email(user):
    """
    Task execution for sending a reset email to the user
    """
    try:
        _set_task_progress(0)
        send_reset_email(user)
    except:
        _set_task_progress(100)


def format_and_save_picture(picture):
    """
    Task execution for formatting/saving an image for the user
    """
    try:
        _set_task_progress(0)
        save_picture(picture)
    except:
        _set_task_progress(100)
