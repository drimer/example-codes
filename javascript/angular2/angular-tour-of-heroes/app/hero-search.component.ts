import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { Subject } from 'rxjs/Subject';

import { Hero } from './hero';
import { HeroSearchService } from './hero-search.service';


@Component({
  moduleId: module.id,
  selector: 'hero-search',
  templateUrl: 'hero-search.component.html',
  styleUrls: ['hero-search.component.css'],
  providers: [HeroSearchService],
})
export class HeroSearchComponent implements OnInit {
  private searchTerms = new Subject<string>();
  private heroes: Observable<Hero[]>;

  constructor(private heroSearchService: HeroSearchService) {}

  ngOnInit(): void {
    this.heroes = this.searchTerms
      .debounceTime(300)
      .distinctUntilChanged()
      .switchMap(term => term
        ? this.heroSearchService.search(term)
        : Observable.of<Hero[]>([])
      )
      .catch(error => {
        console.error(error);
        return Observable.of<Hero[]>([]);
      })
  }

  search(term: string): void {
    this.searchTerms.next(term);
  }
}