export const debounce = (func: Function, wait: number): Function => {
  return (...args: any[]) => {
    const finalCall = () => {
      clearTimeout();
      func(...args);
    }

    clearTimeout();
    setTimeout(finalCall, wait);
  }
}