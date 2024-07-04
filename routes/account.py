from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/acount')
def index():
+    """
+    Renders the 'account.html' template upon accessing the '/account' route.
+    No parameters are passed to this function.
+    Returns the rendered 'account.html' template.
+    """
    return render_template('account.html')