import { TestBed } from '@angular/core/testing';
import { NbpService } from './nbp.service';
import { provideHttpClient } from '@angular/common/http';

describe('NbpService', () => {
  let service: NbpService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [provideHttpClient()]
    });
    service = TestBed.inject(NbpService);
  });

  it('powinien zostac poprawnie utworzony', () => {
    expect(service).toBeTruthy();
  });
});