import java.util.concurrent.TimeUnit;

class Main {
  // adding exception handler into main method
  public static void main(String[] args) throws InterruptedException {

    // creating thread for drink coffee
    Thread drinkCoffee = new Thread(() -> {
      // displaying drink coffee
      System.out.println("drink coffee");
      try {
        // pausing for 1 second
        TimeUnit.SECONDS.sleep(1);
      }
      // catching exception when joining
      catch (InterruptedException e) {
        e.printStackTrace();
      }
    });

    // creating thread for think & talk
    Thread thinkTalk = new Thread(() -> {
      // displaying think
      System.out.println("think");
      try {
        // pausing for 1 second
        TimeUnit.SECONDS.sleep(1);
      }
      // catching exception when joining
      catch (InterruptedException e) {
        e.printStackTrace();
      }
      // displaying talk
      System.out.println("talk");
    });

    // creating thread for eat cookie
    Thread eatCookie = new Thread(() -> {
      // displaying eat cookie
      System.out.println("eat cookie");
      try {
        // pausing for 1 second
        TimeUnit.SECONDS.sleep(1);
      }
      // catching exception when joining
      catch (InterruptedException e) {
        e.printStackTrace();
      }
    });

    // starting threads
    drinkCoffee.start();
    thinkTalk.start();
    eatCookie.start();

    drinkCoffee.join();
    thinkTalk.join();
    eatCookie.join();
  }
}
