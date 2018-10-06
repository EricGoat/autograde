import {Component, OnInit} from '@angular/core'
import axios from 'axios'
import { Task } from './models/task'
import { ServerResponse } from './models/server-response'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'autograde'
  tasks: Task[]

  ngOnInit() {
    axios.request<ServerResponse<Task[]>>({
      url: 'http://localhost:5000/'
    }).then((resp) => {
      this.tasks = resp.data.data
    })
  }

  printData() {
    console.log(this.tasks)
  }
}
