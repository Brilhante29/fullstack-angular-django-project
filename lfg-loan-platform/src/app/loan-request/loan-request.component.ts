import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-loan-request',
  templateUrl: './loan-request.component.html',
  styleUrls: ['./loan-request.component.css'],
})
export class LoanRequestComponent {
  document: string = '';
  name: string = '';
  age: number | null = null;
  income: number | null = null;
  isLoading: boolean = false;

  constructor(private http: HttpClient) {}

  onLoanRequestSubmit() {
    this.isLoading = true;
    const loanRequest = {
      document: this.document,
      name: this.name,
      data: {
        age: this.age,
        income: this.income,
      },
    };
    this.http.post('http://localhost/api/proposals/', loanRequest).subscribe((response) => {
      console.log(response);
      this.isLoading = false;
    });
  }
}
