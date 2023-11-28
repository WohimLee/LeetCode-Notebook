

cpps := $(shell find src -name "*.cpp")
objs := $(patsubst src/%.cpp,objs/%.o,$(cpps))


compile_options := 
linking_options := 

objs/%.o : src/%.cpp
	@echo Compile $^
	@mkdir -p $(dir $@)
	@g++ -c $^ -o $@ $(compile_options)

workspace/exec : $(objs)
	@echo Link $^ to $@
	@mkdir -p $(dir $@)
	@g++ $^ -o $@ $(linking_options)

run : workspace/exec
	@./$<

debug:
	@echo $(cpps)
	@echo $(objs)


clean :
	@rm -rf objs workspace/exec



.PHONY : run debug clean