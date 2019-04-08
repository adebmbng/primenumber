 class PrimeNumberManual {

    /**
     * @param args the command line arguments
     */
    public int totalThread = 5, inputNumber =1003;
     // long start;
    public  static void main(String[] args) {
        // System.out.println(args[1]);
        PrimeNumberManual pn = new PrimeNumberManual();
        pn.inputNumber = Integer.parseInt(args[0]);
        pn.startThread();
        
    }

    private void startThread(){
        long start = System.nanoTime(); 
        PrimeThread pt1 = new PrimeThread(1, totalThread, inputNumber, start);
        PrimeThread pt2 = new PrimeThread(2, totalThread, inputNumber, start);
        PrimeThread pt3 = new PrimeThread(3, totalThread, inputNumber, start);
        PrimeThread pt4 = new PrimeThread(4, totalThread, inputNumber, start);
        PrimeThread pt5 = new PrimeThread(5, totalThread, inputNumber, start);
        pt1.start();
        pt2.start();
        pt3.start();
        pt4.start();
        pt5.start();
         
    }
    
    // private boolean prime(int initNumber){
    //     System.out.println((inputNumber/totalThread));
    //     for(int i =0; i<(inputNumber/totalThread);i++){
    //         int modCalculation = initNumber + (totalThread * i);
    //         if (modCalculation <=3){
    //            // return true;
    //         } else if(modCalculation < inputNumber) {
    //             System.out.println(inputNumber + " "+ modCalculation);
    //             if( (inputNumber % modCalculation) == 0){
    //                 long end = System.nanoTime(); 
    //                 System.out.println((end - start) + " nano");
    //                 return false;
    //             } 
    //         }

    //     }
    //     return true;
    // }
    
}

class PrimeThread implements Runnable {
   private Thread t;
   private int initNumber, totalThread, inputNumber;
   private long start;
   
   PrimeThread( int initNumber, int totalThread, int inputNumber, long start) {
        this.initNumber = initNumber;
        this.totalThread = totalThread;
        this.inputNumber = inputNumber;
        this.start = start;
   }
   
   public void run() {
      System.out.println(this.prime(initNumber));
   }

   private boolean prime(int initNumber){
        // System.out.println((inputNumber/totalThread));
        for(int i =0; i<(inputNumber/totalThread);i++){
            int modCalculation = initNumber + (totalThread * i);
            if (modCalculation <=3){
               // return true;
            } else if(modCalculation < inputNumber) {
                // System.out.println(inputNumber + " "+ modCalculation);
                if( (inputNumber % modCalculation) == 0){
                    long end = System.nanoTime(); 
                    System.out.println(modCalculation + " " +(end - start) + " nano");
                    return false;
                } 
            }

        }
        return true;
    }
   
   public void start () {
      System.out.println("Starting " +  initNumber );
      if (t == null) {
         t = new Thread (this, String.valueOf(initNumber));
         t.start ();
      }
   }
}