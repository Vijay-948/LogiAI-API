package com.peopletech.fractionable.dto.request;

import java.util.Map;
import lombok.Data;

@Data
public class RolesAndPermissionsRequest {
  private Map<String, PermissionDetail> permissions;

  @Data
  public static class PermissionDetail {
    private int id;
    private PermissionValue value;
  }

  @Data
  public static class PermissionValue {
    private int delete;
    private int read;
    private int write;
  }
}
