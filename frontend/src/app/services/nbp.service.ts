import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class NbpService {
  private apiUrl = 'http://127.0.0.1:8000/currencies';

  constructor(private http: HttpClient) {}

  fetchFromNbp(): Observable<any> {
    return this.http.post(`${this.apiUrl}/fetch`, {});
  }

  getCurrencies(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}