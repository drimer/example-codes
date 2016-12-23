import { InMemoryDbService } from 'angular-in-memory-web-api';

export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    let heroes = [
      {id: 11, name: 'Captain America'},
      {id: 12, name: 'Antman'},
      {id: 13, name: 'Doctor Strange'},
      {id: 14, name: 'Hawkeye'},
      {id: 15, name: 'Ironman'},
      {id: 16, name: 'Spiderman'},
      {id: 17, name: 'Superman'},
      {id: 18, name: 'Wonderwoman'},
      {id: 19, name: 'Hulk'},
      {id: 20, name: 'Thor'},
    ];
    return {heroes};
  }
}