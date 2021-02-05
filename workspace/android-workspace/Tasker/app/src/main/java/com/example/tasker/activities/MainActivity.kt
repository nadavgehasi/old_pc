package com.example.tasker.activities

import android.app.AlertDialog
import android.content.DialogInterface
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.example.tasker.data.Task
import com.ramotion.circlemenu.CircleMenuView
import android.widget.LinearLayout
import android.widget.EditText
import com.example.tasker.R
import com.ramotion.foldingcell.FoldingCell
import com.ramotion.foldingcell.views.FoldingCellView
import kotlinx.android.synthetic.main.activity_main.*


class MainActivity : AppCompatActivity() {

    private val tasks: MutableList<Task> = mutableListOf()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val dialogInput: EditText = buildDialogInput()
        val dialog = buildAlertDialog(buildDialogListener(dialogInput), dialogInput)
        buildMenuWithDialog(dialog)

        tasks.add(Task("Most important task ever"))
        tasks.add(Task("Just a regular task"))
        buildTasksList()
    }

    private fun buildTasksList() {
        for (task in tasks)
            addCellToList(convertTaskToFoldingCell(task))
    }

    private fun convertTaskToFoldingCell(task: Task): FoldingCell {
        val foldingCell = FoldingCell(this)
        foldingCell.contentDescription = task.description
        return foldingCell
    }

    private fun addCellToList(foldingCell: FoldingCell) {
        tasksListView.addView(foldingCell)
    }

    private fun buildDialogListener(dialogInput: EditText): DialogInterface.OnClickListener {
        return DialogInterface.OnClickListener { _: DialogInterface, _: Int ->
            addTask(dialogInput.text.toString())
        }
    }

    private fun buildAlertDialog(dialogClickListener: DialogInterface.OnClickListener,
                                 view: View): AlertDialog.Builder? {
        return AlertDialog.Builder(this)
            .setTitle("Create Task")
            .setMessage("Enter the task description")
            .setView(view)
            .setPositiveButton("Create", dialogClickListener)
    }

    private fun buildDialogInput(): EditText {
        val input = EditText(this@MainActivity)
        val lp = LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT,
            LinearLayout.LayoutParams.MATCH_PARENT
        )
        input.layoutParams = lp
        return input
    }

    private fun buildMenuWithDialog(dialog: AlertDialog.Builder?) {
        val menu: CircleMenuView = findViewById(R.id.circle_menu)
        menu.eventListener = object : CircleMenuView.EventListener() {
            override fun onButtonClickAnimationEnd(view: CircleMenuView, buttonIndex: Int) {
                super.onButtonClickAnimationEnd(view, buttonIndex)
                dialog?.show()
            }
        }
    }

    private fun addTask(description: String) {
        tasks.add(Task(description))
    }
}
