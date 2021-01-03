import { Ability } from '../../types/api';
import Fuse from 'fuse.js';

export const useAbilitySearch = (abilities: Ability[], options: Fuse.IFuseOptions<Ability>) => {
  const fuse = new Fuse(abilities, options);

  const search = (searchQuery: string): Ability[] => {
    const results = fuse.search(searchQuery);
    return results.map(res => res.item);
  }

  return search;
}