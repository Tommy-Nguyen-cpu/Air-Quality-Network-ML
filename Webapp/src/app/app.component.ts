import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';

import { FileUploadModule } from 'primeng/fileupload';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule, RouterOutlet,
    FileUploadModule,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Hack to the Rescue!';
  credits = 'Tommy Nguyen & Chris Issa';
  uni = 'Wentworth Institute of Technology';

  api = 'http://127.0.0.1:5000/upload_csv';

  uploadedFiles = []

  onUpload(event: any) {
    // for (let file of event.files) {
    //   this.uploadedFiles.push(file);
    // }
    console.log(event);
  }
}
