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

  onUpload(event: any) {
    const results = event.originalEvent.body.results;
    Object.entries(results).forEach(entry => {
      const [k, v] = entry;

      const new_blob = new Blob([String(v)], {type: 'text/csv'});
      const data = window.URL.createObjectURL(new_blob);
      const link = document.createElement('a');

      link.href = data;
      link.download = k;
      link.click();
    })
  }
}
