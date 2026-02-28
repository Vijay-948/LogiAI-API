package com.peopletech.fractionable.dto.request;

import lombok.Data;

@Data
public class LoginRequestDto {
  private String username;
  private String password;
  private Boolean flag;
}
