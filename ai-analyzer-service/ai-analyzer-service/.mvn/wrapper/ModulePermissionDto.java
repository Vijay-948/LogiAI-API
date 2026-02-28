package com.peopletech.fractionable.dto.request;

import com.peopletech.fractionable.dto.ModuleAndSubModuleMappingDto;
import com.peopletech.fractionable.dto.RolesAndPermissionsDto;
import java.util.List;
import lombok.Data;

@Data
public class ModulePermissionDto {
  private Integer id;
  private RolesAndPermissionsDto value;
  private List<ModuleAndSubModuleMappingDto> subModules;
}
