from taskmanager import db

class Category(db.Model):
    
   #schema for name model
   id = db.Column(db.Integer, primary_key=True)
   manager_name = db.Column(db.string(25), unquie=True, nullable=False)

   def __repr__(self):
       #represent itslef in the form of a  string 
       return self.manager_name

class Task (db.Model):
    #schema for task model
    id = db.Column(db.Integer, primary_key=True)
    task_manager = db.Column(db.string(30), unquie=True, nullable=False)
    task_name = db.Column(db.string(100), unquie=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.date, default=False, nullable=False)
    category_id = db.cloumn(db.Integer, db.Foreignkey("category_id", ondelete="CASCADE"), nullable=False)


    def jls_extract_def(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
                   self.id, self.task_name, self.is_urgent
               )

    def __repr__(self):
       #represent itslef in the form of a  string 
       return self.jls_extract_def() 
       





