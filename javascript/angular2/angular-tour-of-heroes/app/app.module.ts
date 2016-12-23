import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'

import { HeroesComponent } from './heroes.component';
import { HeroDetailComponent } from './hero-detail.component';


@NgModule({
  imports: [ BrowserModule, FormsModule ],
  declarations: [ HeroesComponent, HeroDetailComponent ],
  bootstrap: [ HeroesComponent ]
})
export class AppModule {}
