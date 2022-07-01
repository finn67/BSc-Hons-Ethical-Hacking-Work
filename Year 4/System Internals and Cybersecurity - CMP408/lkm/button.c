#include <linux/module.h>
#include <linux/init.h>
#include <linux/gpio.h>
#include <linux/interrupt.h>
/* Meta Information */
MODULE_LICENSE("GPL");
MODULE_AUTHOR("finlay reid");
MODULE_DESCRIPTION("button lkm");


unsigned int irq_number;

static irq_handler_t gpio_irq_handler(unsigned int irq, void *dev_id, struct pt_regs *regs){
	
	int result = 0;
   	char cmd_path[] = "/usr/bin/python3";
   	char *cmd_argv[] = {cmd_path, "/home/pi/miniproject/temp2.py", NULL};
   	char *cmd_envp[] = {"HOME=/", "PATH=/sbin:/bin:/user/bin", NULL};
   	printk("gpio_irq: interrupt was triggered ans isr was called");
	result = call_usermodehelper(cmd_path, cmd_argv, cmd_envp, UMH_WAIT_PROC);
	return(irq_handler_t) IRQ_HANDLED;



}



/**
 * @brief This function is called, when the module is loaded into the kernel
 */
static int __init ModuleInit(void) {
	printk("gpio_irq: loading module");
	
	
	/* GPIO 17 init */
	if(gpio_request(21, "rpi-gpio-21")) {
		printk("Can not allocate GPIO 21\n");
		return -1;
	}

	/* Set GPIO 17 direction */
	if(gpio_direction_input(21)) {
		printk("Can not set GPIO 21 to input!\n");
		gpio_free(21);
		return -1;
	}

	irq_number = gpio_to_irq(21);

	if(request_irq(irq_number, (irq_handler_t) gpio_irq_handler, IRQF_TRIGGER_RISING, "my_gpio_irq", NULL) !=0){

	printk("Error can not request interrupt nr.: %d\n", irq_number);
	gpio_free(21);
	return -1;

	}

	printk("done/n");
	printk("gpio 21 is mapped to IRQ Nr.: %d\n", irq_number);
	return 0;


}

/**
 * @brief This function is called, when the module is removed from the kernel
 */
static void __exit ModuleExit(void) {
	printk("Goodbye, Kernel\n");
	free_irq(irq_number, NULL);
	gpio_free(21);
}

module_init(ModuleInit);
module_exit(ModuleExit);
