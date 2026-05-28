import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NbpService } from './services/nbp.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  currencies: any[] = [];
  message: string = '';

  constructor(private nbpService: NbpService) {}

  ngOnInit() {
    this.loadCurrencies();
  }

  loadCurrencies() {
    this.nbpService.getCurrencies().subscribe(data => {
      this.currencies = data;
    });
  }

  fetchNewData() {
    this.nbpService.fetchFromNbp().subscribe(res => {
      this.message = res.message; 
      this.loadCurrencies();      
    });
  }
}