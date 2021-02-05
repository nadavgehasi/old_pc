package com.example.learnjetpack

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.compose.Composable
import androidx.compose.unaryPlus
import androidx.ui.core.Clip
import androidx.ui.core.Text
import androidx.ui.core.dp
import androidx.ui.core.setContent
import androidx.ui.foundation.DrawImage
import androidx.ui.foundation.shape.corner.RoundedCornerShape
import androidx.ui.layout.*
import androidx.ui.material.*
import androidx.ui.material.surface.Card
import androidx.ui.res.imageResource
import androidx.ui.text.style.TextOverflow

class MainActivity : AppCompatActivity() {

    private val tasks: MutableList<Task> = mutableListOf()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val task = Task("Pasten")
        tasks.add(task)
        setContent {
            myApp(tasks)
        }
    }

    @Composable
    fun myApp(tasks: MutableList<Task>) {
        MaterialTheme {
            Column {
                Text("Tasks: ")
                generateTasks(tasks = tasks)
                Button(text = "Add", onClick = {tasks.add(Task("asd"))})
            }
        }
    }

    @Composable
    fun generateTasks(tasks: MutableList<Task>) {
        for (task in tasks) {
            createTask(task)
        }
    }

    @Composable
    private fun createTask(task: Task) {
        Card(shape = RoundedCornerShape(8.dp)) {
            Padding(padding = 16.dp) {
                Container(height = 200.dp, expanded = true) {
                    Text(task.description)
                }
            }
        }
    }

//    @Composable
//    fun newsStory(state: Task) {
//        val image = +imageResource(R.drawable.header)
//        MaterialTheme {
//            Column(
//                crossAxisSize = LayoutSize.Expand,
//                modifier=Spacing(16.dp)
//            ) {
//                Container(expanded = true, height = 180.dp) {
//                    Clip(shape = RoundedCornerShape(8.dp)) {
//                        DrawImage(image)
//                    }
//                }
//
//                HeightSpacer(16.dp)
//
//                Text("A day wandering through the sandhills in Shark " +
//                        "Fin Cove, and a few of the sights I saw",
//                    maxLines = 2, overflow = TextOverflow.Ellipsis,
//                    style = (+themeTextStyle { h6 }).withOpacity(0.87f))
//                Text("Davenport, California",
//                    style = (+themeTextStyle { body2 }).withOpacity(0.87f))
//                Text("December 2018",
//                    style = (+themeTextStyle { body2 }).withOpacity(0.6f))
//            }
//        }
//    }
}
