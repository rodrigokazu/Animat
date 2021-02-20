#include <stdlib.h>
#include "objects.h"
#include <ctime>
#include <time.h>

#include "run.h"
#include "brianlib/common_math.h"
#include "randomkit.h"

#include "code_objects/neurongroup_group_variable_set_conditional_codeobject.h"
#include "code_objects/neurongroup_resetter_codeobject.h"
#include "code_objects/neurongroup_thresholder_codeobject.h"


#include <iostream>
#include <fstream>
#include <string>




int main(int argc, char **argv)
{
        

	brian_start();
        

	{
		using namespace brian;

		
                
        _array_defaultclock_dt[0] = 0.0001;
        _array_defaultclock_dt[0] = 0.0001;
        _array_defaultclock_dt[0] = 0.0001;
        _run_neurongroup_group_variable_set_conditional_codeobject();
        _array_defaultclock_timestep[0] = 0;
        _array_defaultclock_t[0] = 0.0;
        magicnetwork.clear();
        magicnetwork.add(&defaultclock, _run_neurongroup_thresholder_codeobject);
        magicnetwork.add(&defaultclock, _run_neurongroup_resetter_codeobject);
        magicnetwork.run(0.1, NULL, 10.0);

	}
        

	brian_end();
        

	return 0;
}