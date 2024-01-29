#!/bin/bash

command_completion() {
  COMPREPLY=($(compgen -W "$1" -- $2))
}

declare -A resource_subcommands_arguments=(
  ["list-providers"]="-h --help --json-output --yaml-output"
  ["get-provider"]="-h --help --cloud_provider_id --json-output --yaml-output"
  ["list-provider-availability-zones"]="-h --help --cloud_provider_id --json-output --yaml-output"
  ["get-provider-availability-zone"]="-h --help --cloud_provider_id --availability_zone_id --json-output --yaml-output"
  ["list-provider-machine-types"]="-h --help --cloud_provider_id --json-output --yaml-output"
  ["get-provider-machine-type"]="-h --help --cloud_provider_id --machine_type_id --json-output --yaml-output"
  ["list-disk-machine-types"]="-h --help --json-output --yaml-output"
  ["list-credential-types"]="-h --help --json-output --yaml-output"
  ["list-engine-cluster-instance-status"]="-h --help --json-output --yaml-output"
  ["list-spark-compute-types"]="-h --help --json-output --yaml-output"
  ["list-spark-infra-versions"]="-h --help --json-output --yaml-output"
  ["list-spark-job-status"]="-h --help --json-output --yaml-output"
  ["list-workflow-execution-states"]="-h --help --json-output --yaml-output"
  ["list-workflow-types"]="-h --help --json-output --yaml-output"
  ["create-volume-conf"]="-h --help --name --description --encrypted --size --disk_type_id --machine_volume_num --machine_volume_strip_num --json-output --yaml-output"
  ["get-volume-conf"]="-h --help --volume_conf_id --volume_conf_name --json-output --yaml-output"
  ["list-volume-confs"]="-h --help --page_number --limit --json-output --yaml-output"
  ["search-volume-confs"]="-h --help --volume_conf_name --page_number --limit --json-output --yaml-output"
  ["edit-volume-conf"]="-h --help --volume_conf_id --volume_conf_name --name --description --encrypted --machine_volume_num --machine_volume_strip_num --json-output --yaml-output"
  ["delete-volume-conf"]="-h --help --volume_conf_id --volume_conf_name --json-output --yaml-output"
  ["create-network-conf"]="-h --help --name --description --network_project_id --network_name --network_tags --subnet --availability_zone_id --json-output --yaml-output"
  ["list-network-confs"]="-h --help --cloud_provider --page_number --limit --json-output --yaml-output"
  ["search-network-confs"]="-h --help --network_conf_name --cloud_provider --page_number --limit --json-output --yaml-output"
  ["get-network-conf"]="-h --help --network_conf_id --network_conf_name --json-output --yaml-output"
  ["edit-network-conf"]="-h --help --network_conf_id --network_conf_name --name --network_project_id --network_name --availability_zone_id --subnet --network_tags --json-output --yaml-output"
  ["create-boot-disk-image-conf"]="-h --help --name --description --cloud_provider_id --linux_distro_id --boot_disk_image --json-output --yaml-output"
  ["get-boot-disk-image-conf"]="-h --help --boot_disk_image_id --boot_disk_image_name --json-output --yaml-output"
  ["list-boot-disk-image-confs"]="-h --help --cloud_provider --page_number --limit --json-output --yaml-output"
  ["search-boot-disk-image-confs"]="-h --help --boot_disk_image_name --cloud_provider --page_number --limit --json-output --yaml-output"
  ["edit-boot-disk-image-conf"]="-h --help --boot_disk_image_id --boot_disk_image_name --name --description --linux_distro_id --boot_disk_image --json-output --yaml-output"
  ["delete-boot-disk-image-conf"]="-h --help --boot_disk_image_id --boot_disk_image_name --json-output --yaml-output"
  ["create-credential-conf"]="-h --help --name --description --credential_type_id --base64_encoded_credentials --json-output --yaml-output"
  ["list-credential-confs"]="-h --help --cloud_provider --page_number --limit --json-output --yaml-output"
  ["search-credential-confs"]="-h --help --credentials_conf_name --cloud_provider --page_number --limit --json-output --yaml-output"
  ["get-credential-conf"]="-h --help --credentials_conf_id --credentials_conf_name --json-output --yaml-output"
  ["edit-credential-conf"]="-h --help --credentials_conf_id --credentials_conf_name --name --description --base64_encoded_credentials --json-output --yaml-output"
  ["delete-credential-conf"]="-h --help --credentials_conf_id --credentials_conf_name --json-output --yaml-output"
  ["create-cloud-env"]="-h --help --name --description --cloud_provider_id --availability_zone_id --network_conf_id --cloud_project --credential_config_id --boot_disk_image_id --json-output --yaml-output"
  ["list-cloud-envs"]="-h --help --cloud_provider --page_number --limit --json-output --yaml-output"
  ["search-cloud-envs"]="-h --help --cloud_env_name --cloud_provider --page_number --limit --json-output --yaml-output"
  ["get-cloud-env"]="-h --help --cloud_env_id --cloud_env_name --json-output --yaml-output"
  ["edit-cloud-env"]="-h --help --cloud_env_id --cloud_env_name --name --description --availability_zone_id --network_conf_id --cloud_project --credential_config_id --boot_disk_image_id --json-output --yaml-output"
  ["delete-cloud-env"]="-h --help --cloud_env_id --cloud_env_name --json-output --yaml-output"
  ["create-object-storage-manager"]="-h --help --name --description --credentials_conf_id --object_storage_bucket_name --json-output --yaml-output"
  ["get-object-storage-manager"]="-h --help --object_storage_manager_id --object_storage_manager_name --json-output --yaml-output"
  ["list-object-storage-managers"]="-h --help --cloud_provider --page_number --limit --json-output --yaml-output"
  ["search-object-storage-managers"]="-h --help --object_storage_manager_name --cloud_provider --page_number --limit --json-output --yaml-output"
  ["edit-object-storage-manager"]="-h --help --object_storage_manager_id --object_storage_manager_name --name --description --credentials_conf_id --object_storage_bucket_name --json-output --yaml-output"
  ["delete-object-storage-manager"]="-h --help --object_storage_manager_id --object_storage_manager_name --json-output --yaml-output"
  ["create-object-storage-manager-file"]="-h --help --object_storage_manager_id --object_storage_manager_name --cluster_id --cluster_name --local_file_path --overwrite --json-output --yaml-output"
  ["list-object-storage-manager-files"]="-h --help --object_storage_manager_id --object_storage_manager_name --page_number --limit --json-output --yaml-output"
  ["search-object-storage-manager-files"]="-h --help --file_name --object_storage_manager_id --object_storage_manager_name --page_number --limit --json-output --yaml-output"
  ["get-object-storage-manager-file"]="-h --help --object_storage_manager_id --object_storage_manager_name --file_id --file_name --json-output --yaml-output"
  ["delete-object-storage-manager-file"]="-h --help --object_storage_manager_id --object_storage_manager_name --file_id --file_name --json-output --yaml-output"
  ["create-hive-metastore-conf"]="-h --help --name --hive_site_xml_file_path --core_site_xml_file_path --hdfs_site_xml_file_path --krb5_conf_file_path --json-output --yaml-output"
  ["list-hive-metastore-confs"]="-h --help --page_number --limit --json-output --yaml-output"
  ["search-hive-metastore-confs"]="-h --help --hive_metastore_conf_name --page_number --limit --json-output --yaml-output"
  ["get-hive-metastore-conf"]="-h --help --hive_metastore_conf_id --hive_metastore_conf_name --json-output --yaml-output"
  ["edit-hive-metastore-conf"]="-h --help --hive_metastore_conf_id --hive_metastore_conf_name --name --hive_site_xml_file_path --core_site_xml_file_path --hdfs_site_xml_file_path --krb5_conf_file_path --json-output --yaml-output"
  ["delete-hive-metastore-conf"]="-h --help --hive_metastore_conf_id --hive_metastore_conf_name --json-output --yaml-output"
)

declare -A cluster_subcommands_arguments=(
  ["create-conf"]="-h --help --name --description --machine_type_category_id --machine_type_id --volume_conf_id --json-output --yaml-output"
  ["list-confs"]="-h --help --cloud_provider --compute_type --page_number --limit --json-output --yaml-output"
  ["search-confs"]="-h --help --cluster_conf_name --cloud_provider --compute_type --page_number --limit --json-output --yaml-output"
  ["get-conf"]="-h --help --cluster_conf_id --cluster_conf_name --json-output --yaml-output"
  ["edit-conf"]="-h --help --cluster_conf_id --cluster_conf_name --name --description --machine_type_category_id --machine_type_id --volume_conf_id --json-output --yaml-output"
  ["delete-conf"]="-h --help --cluster_conf_id --cluster_conf_name --json-output --yaml-output"
  ["create"]="-h --help --name --description --idle_timeout_ms --auto_shutdown --labels --is_spot_instance --enable_public_ip --block_project_ssh_keys --bootstrap_shell_script_file_path --cloud_env_id --object_storage_manager_id --conf --packages --repositories --jars --archives --env_var --conf_secret --env_var_secret --hive_metastore_conf_id --spark_infra_version_id --max_parallel_spark_job_execution_per_instance --standalone_workers_number --cluster_type --min_instances --max_instances --cluster_conf_id --json-output --yaml-output"
  ["list"]="-h --help --cluster_status --cluster_conf_id --cluster_conf_name --page_number --limit --json-output --yaml-output"
  ["search"]="-h --help --cluster_name --page_number --limit --json-output --yaml-output"
  ["get"]="-h --help --cluster_id --cluster_name --json-output --yaml-output"
  ["start"]="-h --help --cluster_id --cluster_name --json-output --yaml-output"
  ["stop"]="-h --help --cluster_id --cluster_name --json-output --yaml-output"
  ["destroy"]="-h --help --cluster_id --cluster_name --json-output --yaml-output"
  ["get-stats"]="-h --help --cluster_id --cluster_name --json-output --yaml-output"
  ["edit"]="-h --help --cluster_id --cluster_name --name --description --idle_timeout_ms --auto_shutdown --labels --enable_public_ip --block_project_ssh_keys --bootstrap_shell_script_file_path --cloud_env_id --object_storage_manager_id --hive_metastore_conf_id --spark_infra_version_id --cluster_conf_id --conf --packages --repositories --jars --archives --env_var --conf_secret --env_var_secret --max_parallel_spark_job_execution_per_instance --standalone_workers_number --min_instances --max_instances --json-output --yaml-output"
  ["list-status"]="-h --help --cluster_id --cluster_name --page_number --limit --json-output --yaml-output"
  ["logs"]="-h --help --cluster_id --cluster_name --log_type --json-output --yaml-output"
  ["associate-workspace"]="-h --help --workspace_id --cluster_id --json-output --yaml-output"
  ["dissociate-workspace"]="-h --help --workspace_id --cluster_id --json-output --yaml-output"
  ["list-workspaces"]="-h --help --cluster_id --page_number --limit --json-output --yaml-output"
  ["list-workspace-clusters"]="-h --help --workspace_id --cluster_status --job_type --page_number --limit --json-output --yaml-output"
  ["search-workspace-clusters"]="-h --help --workspace_id --cluster_name --cluster_status --job_type --page_number --limit --json-output --yaml-output"
)

declare -A workspace_subcommands_arguments=(
  ["create"]="-h --help --name --description --json-output --yaml-output"
  ["list"]="-h --help --enable --page_number --limit --json-output --yaml-output"
  ["search"]="-h --help --workspace_name --enable --page_number --limit --json-output --yaml-output"
  ["get"]="-h --help --workspace_id --workspace_name --json-output --yaml-output"
  ["edit"]="-h --help --workspace_id --workspace_name --name --description --json-output --yaml-output"
  ["enable"]="-h --help --workspace_id --workspace_name --json-output --yaml-output"
  ["disable"]="-h --help --workspace_id --workspace_name --json-output --yaml-output"
  ["create-user-access"]="-h --help --workspace_id --user_id --permission_id --json-output --yaml-output"
  ["create-group-access"]="-h --help --workspace_id --group_id --permission_id --json-output --yaml-output"
  ["delete-user-access"]="-h --help --workspace_id --user_id --permission_id --json-output --yaml-output"
  ["delete-group-access"]="-h --help --workspace_id --group_id --permission_id --json-output --yaml-output"
  ["list-users"]="-h --help --workspace_id --group_id --page_number --limit --json-output --yaml-output"
  ["list-users-access"]="-h --help --workspace_id --permission_id --page_number --limit --json-output --yaml-output"
  ["search-users"]="-h --help --workspace_id --username --group_id --page_number --limit --json-output --yaml-output"
  ["match-user"]="-h --help --workspace_id --username --json-output --yaml-output"
  ["list-groups"]="-h --help --workspace_id --user_id --page_number --limit --json-output --yaml-output"
  ["list-groups-access"]="-h --help --workspace_id --permission_id --page_number --limit --json-output --yaml-output"
  ["search-groups"]="-h --help --workspace_id --groupname --user_id --page_number --limit --json-output --yaml-output"
  ["match-group"]="-h --help --workspace_id --groupname --json-output --yaml-output"
  ["get-user-access"]="-h --help --workspace_id --user_id --json-output --yaml-output"
  ["get-group-access"]="-h --help --workspace_id --group_id --json-output --yaml-output"
)

declare -A job_subcommands_arguments=(
  ["create-conf"]="-h --help --cluster_id --cluster_name --workspace_id --name --files --properties-file --conf --packages --repositories --jars --archives --driver-memory --driver-java-options --driver-library-path --driver-class-path --executor-memory --driver-cores --total-executor-cores --executor-cores --num-executors --principal --keytab --queue --job-type --job-class-name --job-command --job-arguments --job-raw-scala-code --max_concurrency --json-output --yaml-output"
  ["list-confs"]="-h --help --workspace_id --enable --page_number --limit --json-output --yaml-output"
  ["search-confs"]="-h --help --workspace_id --job_conf_name --enable --page_number --limit --json-output --yaml-output"
  ["get-conf"]="-h --help --workspace_id --job_conf_id --job_conf_name --json-output --yaml-output"
  ["edit-conf"]="-h --help --workspace_id --job_conf_id --job_conf_name --cluster_id --cluster_name --files --properties-file --conf --packages --repositories --jars --archives --driver-memory --driver-java-options --driver-library-path --driver-class-path --executor-memory --driver-cores --total-executor-cores --executor-cores --num-executors --principal --keytab --queue --job-class-name --name --job-command --job-arguments --job-raw-scala-code --max_concurrency --json-output --yaml-output"
  ["enable-conf"]="-h --help --workspace_id --job_conf_id --job_conf_name --json-output --yaml-output"
  ["disable-conf"]="-h --help --workspace_id --job_conf_id --job_conf_name --json-output --yaml-output"
  ["start"]="-h --help --workspace_id --job_conf_id --job_conf_name --json-output --yaml-output"
  ["list"]="-h --help --workspace_id --cluster_id --job_conf_id --job_conf_name --job_status --job_type --page_number --limit --json-output --yaml-output"
  ["search"]="-h --help --workspace_id --job_conf_name --cluster_id --job_status --job_type --page_number --limit --json-output --yaml-output"
  ["get"]="-h --help --job_id --workspace_id --json-output --yaml-output"
  ["stop"]="-h --help --job_id --workspace_id --json-output --yaml-output"
  ["get-workflow-job-instance"]="-h --help --job_application_id --workspace_id --json-output --yaml-output"
  ["get-status"]="-h --help --job_id --workspace_id --json-output --yaml-output"
  ["logs"]="-h --help --workspace_id --job_id --log_type --json-output --yaml-output"
)

declare -A notebook_subcommands_arguments=(
  ["create-conf"]="-h --help --json-output --yaml-output --workspace_id --cluster_id --cluster_name --notebook_name --notebook_type --conf --jars --packages --files --driver-memory --executor-memory --driver-cores --total-executor-cores --executor-cores --num-executors"
  ["list-confs"]="-h --help --json-output --yaml-output --workspace_id --enable --page_number --limit"
  ["search-confs"]="-h --help --json-output --yaml-output --workspace_id --notebook_name --enable --page_number --limit"
  ["get-conf"]="-h --help --json-output --yaml-output --workspace_id --notebook_conf_id --notebook_name"
  ["edit-conf"]="-h --help --json-output --yaml-output --workspace_id --notebook_conf_id --notebook_name --cluster_id --cluster_name --name --conf --packages --jars --files --driver-memory --executor-memory --driver-cores --total-executor-cores --executor-cores --num-executors"
  ["enable-conf"]="-h --help --json-output --yaml-output --workspace_id --notebook_conf_id --notebook_name"
  ["disable-conf"]="-h --help --json-output --yaml-output --workspace_id --notebook_conf_id --notebook_name"
  ["start"]="-h --help --json-output --yaml-output --workspace_id --notebook_conf_id --notebook_name"
  ["kernel-start"]="-h --help --json-output --yaml-output --workspace_id --notebook_id"
  ["kernel-interrupt"]="-h --help --json-output --yaml-output --workspace_id --notebook_id"
  ["kernel-restart"]="-h --help --json-output --yaml-output --workspace_id --notebook_id"
  ["list"]="-h --help --json-output --yaml-output --workspace_id --cluster_id --notebook_conf_id --notebook_name --notebook_status --page_number --limit"
  ["search"]="-h --help --json-output --yaml-output --workspace_id --notebook_name --page_number --limit"
  ["get"]="-h --help --json-output --yaml-output --workspace_id --notebook_id"
  ["stop"]="-h --help --json-output --yaml-output --workspace_id --notebook_id"
  ["logs"]="-h --help --json-output --yaml-output --workspace_id --notebook_id --log_type"
)

declare -A iam_subcommands_arguments=(
  ["list-tenants"]="-h --help --page_number --limit --json-output --yaml-output"
  ["associate-tenant"]="-h --help --tenant_id --json-output --yaml-output"
  ["get-user-info"]="-h --help --json-output --yaml-output"
  ["get-user-roles"]="-h --help --json-output --yaml-output"
  ["sync-user"]="-h --help --username --json-output --yaml-output"
  ["sync-group"]="-h --help --groupname --json-output --yaml-output"
  ["list-user-groups"]="-h --help --user_id --page_number --limit --json-output --yaml-output"
  ["list-users"]="-h --help --group_id --page_number --limit --json-output --yaml-output"
  ["list-group-users"]="-h --help --group_id --page_number --limit --json-output --yaml-output"
  ["list-groups"]="-h --help --user_id --page_number --limit --json-output --yaml-output"
  ["search-users"]="-h --help --username --group_id --page_number --limit --json-output --yaml-output"
  ["match-user"]="-h --help --username --json-output --yaml-output"
  ["match-group"]="-h --help --groupname --json-output --yaml-output"
  ["search-groups"]="-h --help --groupname --user_id --page_number --limit --json-output --yaml-output"
  ["list-resources"]="-h --help --json-output --yaml-output"
  ["get-resource"]="-h --help --resource_id --json-output --yaml-output"
  ["list-permissions"]="-h --help --json-output --yaml-output"
  ["get-permission"]="-h --help --permission_id --json-output --yaml-output"
  ["list-roles"]="-h --help --json-output --yaml-output"
  ["get-role"]="-h --help --role_id --json-output --yaml-output"
  ["list-rules"]="-h --help --json-output --yaml-output"
  ["get-rule"]="-h --help --rule_id --json-output --yaml-output"
  ["list-workspace-permissions"]="-h --help --json-output --yaml-output"
  ["get-workspace-permission"]="-h --help --permission_id --json-output --yaml-output"
)

declare -A admin_subcommands_arguments=(
  ["list-users"]="-h --help --json-output --yaml-output --page_number --limit"
  ["search-users"]="-h --help --json-output --yaml-output --username --page_number --limit"
  ["get-user"]="-h --help --json-output --yaml-output --user_id"
  ["get-user-roles"]="-h --help --json-output --yaml-output --user_id"
  ["list-users-roles"]="-h --help --json-output --yaml-output --page_number --limit"
  ["get-role-users"]="-h --help --json-output --yaml-output --role_id --page_number --limit"
  ["list-groups"]="-h --help --json-output --yaml-output --page_number --limit"
  ["search-groups"]="-h --help --json-output --yaml-output --groupname --page_number --limit"
  ["get-group"]="-h --help --json-output --yaml-output --group_id"
  ["get-group-roles"]="-h --help --json-output --yaml-output --group_id"
  ["list-groups-roles"]="-h --help --json-output --yaml-output --page_number --limit"
  ["get-role-groups"]="-h --help --json-output --yaml-output --role_id --page_number --limit"
  ["create-user-role"]="-h --help --json-output --yaml-output --user_id --role_id"
  ["delete-user-role"]="-h --help --json-output --yaml-output --user_id --role_id"
  ["create-group-role"]="-h --help --json-output --yaml-output --group_id --role_id"
  ["delete-group-role"]="-h --help --json-output --yaml-output --group_id --role_id"
)

declare -A platform_admin_subcommands_arguments=(
  ["create-tenant"]="-h --help --name --description --json-output --yaml-output"
  ["list-tenants"]="-h --help --page_number --limit --json-output --yaml-output"
  ["get-tenant"]="-h --help --tenant_id --tenant_name --json-output --yaml-output"
  ["delete-tenant"]="-h --help --tenant_id --tenant_name --json-output --yaml-output"
  ["edit-tenant"]="-h --help --tenant_id --tenant_name --name --description --json-output --yaml-output"
  ["search-tenants"]="-h --help --tenant_name --page_number --limit --json-output --yaml-output"
  ["list-user-tenants"]="-h --help --name --description --json-output --yaml-output"
  ["list-tenant-users"]="-h --help --json-output --yaml-output --tenant_id --page_number --limit"
  ["search-tenant-users"]="-h --help --json-output --yaml-output --tenant_id --username --page_number --limit"
  ["get-tenant-user"]="-h --help --json-output --yaml-output --tenant_id --user_id"
  ["get-user-roles"]="-h --help --json-output --yaml-output --tenant_id --user_id"
  ["list-users-roles"]="-h --help --json-output --yaml-output --tenant_id --page_number --limit"
  ["get-role-users"]="-h --help --json-output --yaml-output --tenant_id --role_id --page_number --limit"
  ["list-tenant-groups"]="-h --help --json-output --yaml-output --tenant_id --page_number --limit"
  ["search-tenant-groups"]="-h --help --json-output --yaml-output --tenant_id --groupname --page_number --limit"
  ["get-tenant-group"]="-h --help --json-output --yaml-output --tenant_id --group_id"
  ["get-group-roles"]="-h --help --json-output --yaml-output --tenant_id --group_id"
  ["list-groups-roles"]="-h --help --json-output --yaml-output --tenant_id --page_number --limit"
  ["get-role-groups"]="-h --help --json-output --yaml-output --tenant_id --role_id --page_number --limit"
  ["create-user-role"]="-h --help --json-output --yaml-output --tenant_id --user_id --role_id"
  ["delete-user-role"]="-h --help --json-output --yaml-output --tenant_id --user_id --role_id"
  ["create-group-role"]="-h --help --json-output --yaml-output --tenant_id --group_id --role_id"
  ["delete-group-role"]="-h --help --json-output --yaml-output --tenant_id --group_id --role_id"
)

_yeedu_completion() {
  local cli_name cmd subcmd cur
  COMPREPLY=()
  cli_name="${COMP_WORDS[0]}"
  cmd="${COMP_WORDS[1]}"
  subcmd="${COMP_WORDS[2]}"
  cur="${COMP_WORDS[COMP_CWORD]}"

  if [[ "$cli_name" == "yeedu" ]]; then
    command_completion "configure resource cluster workspace job notebook iam admin platform-admin logout" $cur

    if [[ "$cmd" == "configure" ]]; then
      command_completion "-h --help --timeout --no-browser --json-output --yaml-output" $cur

    elif [[ "$cmd" == "resource" ]]; then
      command_completion '"${!resource_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${resource_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${resource_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "cluster" ]]; then
      command_completion '"${!cluster_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${cluster_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${cluster_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "workspace" ]]; then
      command_completion '"${!workspace_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${workspace_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${workspace_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "job" ]]; then
      command_completion '"${!job_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${job_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${job_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "notebook" ]]; then
      command_completion '"${!notebook_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${notebook_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${notebook_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "iam" ]]; then
      command_completion '"${!iam_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${iam_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${iam_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "admin" ]]; then
      command_completion '"${!admin_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${admin_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${admin_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "platform-admin" ]]; then
      command_completion '"${!platform_admin_subcommands_arguments[@]}"' $cur

      if [[ -n "$subcmd" && -n "${platform_admin_subcommands_arguments[$subcmd]}" ]]; then
        command_completion "${platform_admin_subcommands_arguments[$subcmd]}" $cur
      fi
    elif [[ "$cmd" == "logout" ]]; then
      command_completion "-h --help --json-output --yaml-output" $cur
    fi
  fi
}

complete -F _yeedu_completion yeedu
